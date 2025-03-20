import tweepy

bearer_token = "AAAAAAAAAAAAAAAAAAAAAKkl0AEAAAAA5s3yGoqI1IxOuGYDZmsdpTsmjBM%3DC8dS2eKd6rrCu3eWVxmj9LtTcrp4pr6alLQlNJ4Mhpb05ZRD50";

#Twitter API用のクライアントを初期化
client = tweepy.Client(bearer_token=bearer_token)

query = "エアドロ"

response = client.search_recent_tweets(
    query=query,
    tweet_fields=["id","text","created_at"],
    max_results=10
)

# if response.data:
#     for tweet in response.data:
#         print(f"ID: {tweet.id}) | 投稿日: {tweet.created_at}\nツイート内容: {tweet.text}\n")
#     else:
#         print("該当するツイートは見つかりませんでした。")

username = "GuildQB"
user_response = client.get_user(username=username, user_fields=["id", "name", "username", "created_at"])
if user_response.data:
    user = user_response.data
    print(f"ユーザーID: {user.id} | 名前: {user.name} | ユーザー名: {user.username}")
else:
    print("ユーザー情報が見つかりませんでした。")

# ユーザーIDからツイートを取得
if user_response.data:
    user_id = user_response.data.id
    tweets_response = client.get_users_tweets(
        id=user_id,
        tweet_fields=["id", "text", "created_at"],
        max_results=5
    )
    if tweets_response.data:
        for tweet in tweets_response.data:
            print(f"ツイートID: {tweet.id} | 投稿日: {tweet.created_at}\n内容: {tweet.text}\n")
    else:
        print("ツイートが見つかりませんでした。")