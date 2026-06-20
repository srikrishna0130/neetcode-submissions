import time
from heapq import *

class Twitter:
    MOST_RECENT = 10
    STEP = 0
    def __init__(self):
        self.userTweets = defaultdict(list)
        self.followable = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.STEP, tweetId])
        self.STEP += 1
    
    def follow(self, userId: int, followingId: int) -> None:
        if userId != followingId and followingId not in self.followable[userId]:
            self.followable[userId].append(followingId)
        self.STEP += 1

    def unfollow(self, userId: int, followingId: int) -> None:
        if userId != followingId and followingId in self.followable[userId]:
            self.followable[userId].remove(followingId)
        self.STEP += 1
    
    def getNewsFeed(self, userId: int) -> list[int]:
        tweets = []

        # get user's tweets
        for t in self.userTweets[userId]:
            heappush(tweets, t)
            if len(tweets) > self.MOST_RECENT:
                heappop(tweets)
        
        for fol in self.followable[userId]:
            for t in self.userTweets[fol]:
                heappush(tweets, t)
                if len(tweets) > self.MOST_RECENT:
                    heappop(tweets)
        
        result = []
        while tweets:
            result.append(heappop(tweets)[1])
        self.STEP += 1
        return result[::-1]