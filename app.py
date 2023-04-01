
import streamlit as st
import requests
import json
import streamlit.components.v1 as components
from jinja2 import Template

def get_apps():
    #url = 'https://lc-opendata01.s3.amazonaws.com/apps.json'
    url = './apps.json'
    if 'https' in url:
        response = requests.get(url)
        result = json.loads(response.text)
    else:
        with open(url) as f:
            result = json.load(f)
    return result

def filter_apps(apps):
    cols = st.columns([1,3])
    result = apps

    with cols[0]:
        form = st.form("🔎 Find")
        with form:
            find_expression = st.text_input("🔎 Find")
            status = st.selectbox('Status',options=['<all>', 'in progress', 'active', 'archived'])
            if form.form_submit_button("Filter"):
                if status != '<all>':
                    result = [obj for obj in apps if obj['status'] == status]
                else:
                    result = apps

                if find_expression:
                    result = [obj for obj in result if find_expression.lower() in (obj['description'] + obj['name']).lower()]
                    
    return result

def render_apps(apps):
    # with open('template.html', 'r') as f:
    #     template_content = f.read()
    #     template = Template(template_content)
    #     html = template.render(apps=filtered_apps)
    # components.html(html, height=10000)
    cols = st.columns(3)
    col=0
    for app in apps:
        with cols[col]:
            if 'url' in app:
                st.markdown(f"### {app['name']}[🚀]({app['url']})")
            else:
                st.markdown(f"### {app['name']}")
            st.markdown(app['description'])
            st.markdown(f"Status: {app['status']}")
            st.markdown(f"[git-repo]({app['git']})") 
        col = col+1 if col < len(cols)-1 else 0

def main():
    st.set_page_config(
    page_title="Lukas Apps",
    page_icon="🤖",
    layout="wide")

    st.markdown("# Lukas' app collection 💻")
    apps = get_apps()
    filtered_apps = filter_apps(apps)
    st.markdown(f"{len(filtered_apps)} apps found")
    st.markdown('<br>',unsafe_allow_html=True)
    render_apps(filtered_apps)
   

if __name__ == '__main__':
    main()


