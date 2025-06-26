# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import pymysql
from sqlalchemy import create_engine
from sqlalchemy import text
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime, timedelta


DB = st.secrets["mysql"]

# ✅ 한글 폰트 설정
font_paths = fm.findSystemFonts(fontext='ttf')
for path in font_paths:
    if 'NanumGothic' in path:
        plt.rcParams['font.family'] = fm.FontProperties(fname=path).get_name()
        break
plt.rcParams['axes.unicode_minus'] = False

# ✅ DB 연결
@st.cache_resource
def get_engine():
    try:
        engine = create_engine(
            f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}?charset={DB['charset']}"
        )
        # st.success("✅ DB 연결 성공") # 성공 메시지는 한번만 표시되도록 제거
        return engine
    except Exception as e:
        st.error(f"🚨 DB 연결 실패: {e}")
        return None

engine = get_engine()

# ✅ 데이터 불러오기 최적화
@st.cache_data(ttl=3600)
def load_data(_engine):
    if _engine is None:
        return pd.DataFrame(), pd.DataFrame()
    # 분석에 필요한 최소한의 데이터만 로드하여 속도 개선
    # 인기 영상 및 날짜별 분석을 위해 조회수 상위 200개 영상 로드
    videos_query = """
        SELECT video_id, channel_id, title, view_count, like_count, comment_count, published_at
        FROM videos
        ORDER BY view_count DESC
        LIMIT 200
    """
    videos = pd.read_sql(videos_query, _engine)

    # 최근 댓글 분석을 위해 최신 100개 댓글 로드
    comments_query = """
        SELECT video_id, author_display_name, text_display, published_at
        FROM comments
        ORDER BY published_at DESC
        LIMIT 100
    """
    comments = pd.read_sql(comments_query, _engine)

    if not videos.empty:
        videos['published_at'] = pd.to_datetime(videos['published_at'])
    if not comments.empty:
        comments['published_at'] = pd.to_datetime(comments['published_at'])

    return videos, comments

# ✅ 총 영상/댓글 수 가져오기 (별도 캐시)
@st.cache_data(ttl=600)
def get_total_counts(_engine):
    if _engine is None:
        return 0, 0
    with _engine.connect() as conn:
        total_videos = conn.execute(text("SELECT COUNT(*) FROM videos")).scalar()
        total_comments = conn.execute(text("SELECT COUNT(*) FROM comments")).scalar()
    return total_videos, total_comments

# ✅ Streamlit 레이아웃 구성
st.set_page_config(layout="wide", page_title="국가유산 콘텐츠 대시보드")
st.title("📊 국가유산 유튜브 콘텐츠 수집 대시보드")

if engine:
    videos_df, comments_df = load_data(engine)

    # 데이터 로딩 실패 시 경고
    if videos_df.empty or comments_df.empty:
        st.warning("⚠️ 데이터를 불러오는 데 실패했거나 테이블에 데이터가 없습니다.")
        st.stop()

    # ✅ 상단 요약 지표
    total_videos, total_comments = get_total_counts(engine)
    col1, col2, col3 = st.columns(3)
    col1.metric("🎞️ 총 영상 수", f"{total_videos:,} 개")
    col2.metric("💬 총 댓글 수", f"{total_comments:,} 개")
    col3.metric("📺 채널 수", f"{videos_df['channel_id'].nunique():,} 개")

    st.markdown("---")

    # ✅ 대시보드 메인 섹션
    col1, col2 = st.columns([2, 3])

    with col1:
        st.subheader("🔥 인기 영상")
        top_n = st.slider("표시할 영상 수", 5, 20, 10, key="top_n_slider")
        top_videos = videos_df.sort_values("view_count", ascending=False).head(top_n)
        st.dataframe(
            top_videos[['title', 'view_count', 'like_count']],
            use_container_width=True,
            hide_index=True,
            column_config={
                "title": st.column_config.TextColumn("제목", width="large"),
                "view_count": st.column_config.NumberColumn("조회수", format="%,d"),
                "like_count": st.column_config.NumberColumn("좋아요", format="%,d"),
            }
        )

    with col2:
        st.subheader("🗓️ 영상 공개일 분포")
        min_date = videos_df['published_at'].min().date()
        max_date = videos_df['published_at'].max().date()
        
        start_date, end_date = st.date_input(
            '날짜 범위 선택',
            (max_date - timedelta(days=90), max_date),
            min_value=min_date,
            max_value=max_date,
            format="YYYY-MM-DD",
            key="date_range_picker"
        )

        if start_date and end_date and start_date <= end_date:
            mask = (videos_df['published_at'].dt.date >= start_date) & (videos_df['published_at'].dt.date <= end_date)
            filtered_videos = videos_df.loc[mask]
            if not filtered_videos.empty:
                daily_counts = filtered_videos.set_index('published_at').resample('D').size()
                st.bar_chart(daily_counts)
            else:
                st.info("선택된 기간에 해당하는 데이터가 없습니다.")
        else:
            st.warning("올바른 날짜 범위를 선택해주세요.")

    st.markdown("---")

    # ✅ 최근 댓글
    st.subheader("📝 최근 수집된 댓글")
    st.dataframe(
        comments_df[['author_display_name', 'text_display', 'published_at']],
        use_container_width=True,
        hide_index=True,
        height=300,
        column_config={
            "author_display_name": "작성자",
            "text_display": "댓글 내용",
            "published_at": st.column_config.DatetimeColumn("작성일", format="YYYY-MM-DD HH:mm"),
        }
    )

    # ✅ 데이터 디버깅 확인 (숨김 처리)
    with st.expander("🔍 원본 데이터 확인"):
        st.write("#### Videos DataFrame (상위 200개)")
        st.dataframe(videos_df)
        st.write("#### Comments DataFrame (최신 100개)")
        st.dataframe(comments_df)
else:
    st.error("🚨 대시보드를 표시할 수 없습니다. DB 연결을 확인하세요.")