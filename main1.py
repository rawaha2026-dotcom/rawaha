from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

# 1. شاشة الترحيب الافتتاحية
class WelcomeScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(text="أهلاً بك في", font_size='20sp', color=(0.4, 0.5, 0.6, 1)))
        layout.add_widget(Label(text="مؤسسة صروح مكينة التعليمية", font_size='26sp', bold=True))
        layout.add_widget(Label(text="برنامج النبراس", font_size='22sp', bold=True, color=(1, 0.6, 0.1, 1)))
        
        btn_enter = Button(text="الدخول إلى البرنامج", font_size='18sp', size_hint=(1, 0.2), background_color=(1, 0.6, 0.1, 1))
        btn_enter.bind(on_press=self.go_to_main)
        layout.add_widget(btn_enter)
        
        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main_menu'

# 2. شاشة قائمة الدورات والتحقق
class MainMenuScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="قائمة الدورات المتاحة", font_size='22sp', bold=True))
        layout.add_widget(Label(text="دورة إضاءات في إدارة الحلقات القرآنية", font_size='16sp', color=(1, 0.6, 0.1, 1)))
        
        btn_part1 = Button(text="الجزء الأول", font_size='18sp', size_hint=(1, 0.15))
        btn_part1.bind(on_press=lambda x: self.show_popup("الجزء الأول"))
        layout.add_widget(btn_part1)
        
        btn_part2 = Button(text="الجزء الثاني", font_size='18sp', size_hint=(1, 0.15))
        btn_part2.bind(on_press=lambda x: self.show_popup("الجزء الثاني"))
        layout.add_widget(btn_part2)
        
        self.add_widget(layout)

    def show_popup(self, part_name):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        box.add_widget(Label(text=f"هل شاهدت {part_name}؟", font_size='16sp'))
        
        buttons = BoxLayout(spacing=10, size_hint=(1, 0.4))
        btn_yes = Button(text="نعم", background_color=(0, 1, 0, 1))
        btn_no = Button(text="لا", background_color=(1, 0, 0, 1))
        
        buttons.add_widget(btn_yes)
        buttons.add_widget(btn_no)
        box.add_widget(buttons)
        
        popup = Popup(title="تأكيد المشاهدة", content=box, size_hint=(0.8, 0.4), auto_dismiss=False)
        
        btn_yes.bind(on_press=lambda x: self.action_yes(popup, part_name))
        btn_no.bind(on_press=lambda x: popup.dismiss())
        
        popup.open()

    def action_yes(self, popup, part_name):
        popup.dismiss()
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(text=f"تم تسجيل إتمام {part_name} بنجاح!\nبارك الله فيك.", font_size='14sp'))
        btn_close = Button(text="موافق", size_hint=(1, 0.4))
        content.add_widget(btn_close)
        
        success_popup = Popup(title="أحسنت", content=content, size_hint=(0.7, 0.3))
        btn_close.bind(on_press=success_popup.dismiss)
        success_popup.open()

class NebrasApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MainMenuScreen(name='main_menu'))
        return sm

if name == 'main':
    NebrasApp().run()
