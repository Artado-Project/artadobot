
from typing import List
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from builders.dbContextBuilder import DbContextBuilder
from helpers.envConfigurator import EnvConfigurator
from models.webSites import WebSites
from repositories.dbContext import DbContext
from repositories.webSiteRepository import WebSiteRespository

load_dotenv()
def CreateModel():
    env = EnvConfigurator()
    url = env.MigrateConfiguration("MYSQL_DB")
    print(url)
    context:DbContext = DbContextBuilder.Build(url, WebSites)
    new_site = WebSites(4, "www.discord.com.tr", True, False, True, True, True, 0)
    print(context.Create(new_site))
    
def GetAll():
    env = EnvConfigurator()
    url = env.MigrateConfiguration("MYSQL_DB")
    context: DbContext = DbContextBuilder.Build(url, WebSites)
    all_sites = context.GetAll()
    for i in all_sites:
        print(i.domain_url)
    
def GetById():
    env = EnvConfigurator()
    url = env.MigrateConfiguration("MYSQL_DB")
    context: DbContext = DbContextBuilder.Build(url, WebSites)
    site:WebSites = context.GetById(4)
    print(f"{site.domain_url}, {site.is_support_android}")

def GetByExpression():
    env = EnvConfigurator()
    url = env.MigrateConfiguration("MYSQL_DB")
    context: DbContext = DbContextBuilder.Build(url, WebSites)
    sites: List = context.GetObjectsWithCondition(
        lambda: WebSites.using_php == False
    )
    for i in sites:
        print(i.domain_url)
def RunTest():
    #CreateModel()
    #GetAll()
    #GetById()
    GetByExpression()