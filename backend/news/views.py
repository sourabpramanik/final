from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from newsapi import NewsApiClient
import requests

newsapi = NewsApiClient(api_key='33823cc13bce49f5b21e9916bc4f09ea')




class topHeadLines(APIView):
    def get(self, request):
    
        topHeadLines= newsapi.get_top_headlines(
                                          sources='bbc-news,the-verge, cnn-news,abcnews, associated-press, axios, bleacher-report, bloomberg, business-insider,cbs-news, crypto-coins-news, entertainment-weekly, espn',
                                          language='en',)

        return Response(topHeadLines)

class Categories(APIView):

    def post(self, request):
        q = request.data.get("category")
        if q == "bitcoin":
            all_articles = newsapi.get_everything(q=q,
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk, techcrunch.com',
                                      from_param='2021-01-02',
                                      to='2021-01-06',
                                      language='en',
                                     
                                      page=2)
            context = {all_articles}
        else:
            context= {"ERROR"}
        return Response(context)
        

