#pip install kivy
#pip install kivymd
#pip install https://github.com/kivymd/KivyMD/archive/3274d62.zip

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock


KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]



    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1

                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Input"
                        
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   
                                
                                BoxLayout:
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                        
                                    MDTextField:
                                        hint_text: "Start date"
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:
                                        icon: "cash"
                                        
                                    MDTextField:
                                        hint_text: "Loan"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                
                                    
                                    MDIconButton:
                                        icon: "clock-time-five-outline"
                                            
                                    MDTextField:
                                        hint_text: "Months"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                 
                                    
                                    MDIconButton:
                                        icon: "bank"
                                            
                                    MDTextField:
                                        hint_text: "Interest, %"
                                    
                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if self.focus: app.menu.open()
                                 
                                 
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"
                        
                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"
                        
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"
                        
                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"
         

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
                
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MortgageCalculatorApp(MDApp):
    title = "Mortgage Calculator"
    by_who = "author Oleg Shpagin"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        #menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "annuity"},
                      {"icon": "format-text-rotation-angle-down", "text": "differentiated"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)

    def build(self):
        # self.theme_cls.theme_style = "Light"  # "Dark"  # "Light"
        # return Builder.load_string(KV)
        return self.screen

    def on_start(self):
        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "youtube": "My YouTube",
            "coffee": "Donate author",
            "github": "Source code",
            "share-variant": "Share app",  #air-horn
            "shield-sun": "Dark/Light",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "Input",  #ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )

        # To auto generate tabs
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(
        #             text=f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/size][/font] {name_tab}"
        #         )
        #     )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        print("tab clicked! " + tab_text)

    def on_star_click(self):
        print("star clicked!")


MortgageCalculatorApp().run()