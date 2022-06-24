import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'
        self.headers= {"apikey": "soJKYZq4ern4UofbC2VKpqVRfCbED4Ac"}
    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json() # json.loads() ile aynı

    def getRepositories(self, username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self, repoName):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.token, json={
            "name": repoName,
            "description": "This is a test creating in Github",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })        

        return response.json()
github = Github()
while True:
    secim = input("1 - Find User\n2 - Get Repositories\n3 - Create Repository\n4 - Exit\n5 - Seçim: ")

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif secim == '3':
            repoName = input('Repository adı: ')
            result = github.createRepository(repoName)
            print(result)
        else:
            print("Yanlış seçim")