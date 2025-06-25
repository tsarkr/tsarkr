# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import pymysql
from sqlalchemy import create_engine
import configparser
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

DB = st.secrets["mysql"]

# ✅ 한글 폰트 설정
font_paths = fm.findSystemFonts(fontext='ttf')
for path in font_paths:
    if 'NanumGothic' in path:
        plt.rcParams['font.family'] = fm.FontProperties(fname=path).get_name()
        break
plt.rcParams['axes.unicode_minus'] = False

# ✅ config.ini 로드
def load_config(path="config.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    return {
        "api_key": config.get("google_api", "api_key"),
        "db_config": {
            "user": config.get("mysql", "user"),
            "password": config.get("mysql", "password"),
            "host": config.get("mysql", "host"),
            "database": config.get("mysql", "database"),
            "charset": config.get("mysql", "charset"),
        }
    }

CONFIG = load_config()
DB = CONFIG["db_config"]

# ✅ DB 연결
@st.cache_resource
def get_engine():
    engine = create_engine(
        f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}?charset={DB['charset']}"
    )
    st.success("✅ DB 연결 성공")
    return engine

engine = get_engine()

# ✅ 데이터 불러오기
@st.cache_data(ttl=300)
def load_data():
    videos = pd.read_sql("SELECT * FROM videos", engine)
    comments = pd.read_sql("SELECT * FROM comments", engine)
    st.write("📥 videos 로딩 완료:", videos.shape)
    st.write("📥 comments 로딩 완료:", comments.shape)
    return videos, comments

videos_df, comments_df = load_data()

# ✅ Streamlit 레이아웃 구성
st.set_page_config(layout="wide", page_title="국가유산 콘텐츠 대시보드")
st.title("📊 국가유산 유튜브 콘텐츠 수집 대시보드")

# ✅ 데이터 디버깅 확인
st.subheader("✅ 로딩된 데이터 상태")
st.write("영상 데이터프레임 크기:", videos_df.shape)
st.write("댓글 데이터프레임 크기:", comments_df.shape)

if videos_df.empty:
    st.warning("⚠️ videos 테이블에 데이터가 없습니다.")
if comments_df.empty:
    st.warning("⚠️ comments 테이블에 데이터가 없습니다.")

# ✅ 상단 요약 지표
col1, col2, col3 = st.columns(3)
col1.metric("🎞️ 총 영상 수", f"{len(videos_df):,} 개")
col2.metric("💬 총 댓글 수", f"{len(comments_df):,} 개")
col3.metric("📺 채널 수", f"{videos_df['channel_id'].nunique():,} 개")

st.markdown("---")

# ✅ 날짜별 수집 영상 수
st.subheader("🗓️ 수집 날짜별 영상 수")
videos_df["crawled_date"] = pd.to_datetime(videos_df["crawled_at"]).dt.date
daily_counts = videos_df.groupby("crawled_date").size()

st.bar_chart(daily_counts)

# ✅ 인기 영상 Top 10
st.subheader("🔥 조회수 기준 인기 영상 Top 10")
top_videos = videos_df.sort_values("view_count", ascending=False).head(10)
st.dataframe(top_videos[["title", "view_count", "like_count", "comment_count", "published_at"]])

# ✅ 최근 댓글 100건 미리보기
st.subheader("📝 최근 수집된 댓글")
recent_comments = comments_df.sort_values("crawled_at", ascending=False).head(100)
st.dataframe(recent_comments[["video_id", "author_display_name", "text_display", "published_at"]])