from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from jnius import autoclass

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.renpy.android.PythonActivity').mActivity

class WebViewApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        wvc = WebViewClient()
        webview.setWebViewClient(wvc)
        webview.loadUrl("http://www.google.com")

        layout.add_widget(webview)
        return layout

if __name__ == '__main__':
    WebViewApp().run()
