import folium
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_map(request: Request):
    # Folium을 사용하여 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)  # 예시로 서울 좌표를 사용

    # 마커 추가
    folium.Marker([37.5665, 126.9780], popup='서울 시청').add_to(m)

    # Folium 맵을 HTML 데이터로 변환
    html_map = m._repr_html_()

    return templates.TemplateResponse("index.html", {"request": request, "map": html_map})