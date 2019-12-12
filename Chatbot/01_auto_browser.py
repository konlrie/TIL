import webbrowser

# webbrowser.open('https://naver.com')

# https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8
# https://search.naver.com/search.naver?query=방탄소년단

artists = ['민수', '방탄소년단', '에일리']
for artist in artists:
    webbrowser.open('https://search.naver.com/search.naver?query=' + artist)
