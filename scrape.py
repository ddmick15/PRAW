import praw
import requests

def get_reddit_posts(keyword, num_posts):
    reddit = praw.Reddit(
        client_id='lwZXEmN-RPzLdKi1Gzrl6g',
        client_secret='SiqyuqJEzl7h4Cq1-_YzvWASP9qmJQ',
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    )

    reddit_posts = []
    for submission in reddit.subreddit("stocks").search(keyword, limit=num_posts):
        reddit_posts.append(submission.title)

    return reddit_posts

if __name__ == "__main__":
    keyword = "nvidia"
    num_posts = 33  # Adjust as needed
    posts = get_reddit_posts(keyword, num_posts)
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post}")

