import streamlit as st
import datetime

# タイトル
st.title("🛠️ 顧客サポートポータル モック")

# FAQ検索バー
st.subheader("🔍 FAQ検索")
faq_query = st.text_input("質問を入力してください")
if st.button("検索"):
    # 仮の回答表示（OpenAI APIと連携可能）
    st.info(f"'{faq_query}' に関するFAQ結果はこちらです：\n- 仮の回答1\n- 仮の回答2")

# 問い合わせフォーム
st.subheader("📨 お問い合わせフォーム")
with st.form("inquiry_form"):
    user_name = st.text_input("お名前")
    email = st.text_input("メールアドレス")
    category = st.selectbox("カテゴリ", ["ログインの問題", "課金・請求", "その他"])
    inquiry = st.text_area("お問い合わせ内容")
    submitted = st.form_submit_button("送信")
    if submitted:
        st.success("お問い合わせを受け付けました。サポートよりご連絡いたします。")

# 過去の問い合わせ履歴（サンプル）
st.subheader("🧾 過去の問い合わせ履歴")
inquiries = [
    {"日付": "2024-12-01", "件名": "ログインできない", "ステータス": "対応中"},
    {"日付": "2024-11-15", "件名": "請求金額について", "ステータス": "完了"},
    {"日付": "2024-10-30", "件名": "パスワード再発行", "ステータス": "完了"},
]
st.table(inquiries)

# チャット風UI（シンプルモック）
st.subheader("💬 チャットサポート（モック）")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("メッセージを入力してください")
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    # 仮のAI応答（OpenAIと連携可）
    response = "お問い合わせありがとうございます。担当者が確認中です。"
    st.session_state.chat_history.append(("ai", response))

for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

# フッター
st.markdown("---")
st.caption("© 2025 顧客サポートチーム モックデモ")
