import requests

class InternetInfo:

  def api_saman_caribbean():
    url = "https://saman-caribbean.vercel.app/api/cruise-ships"
    response = requests.request("GET",url)
    return response.json()