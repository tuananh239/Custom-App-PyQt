
#title_bar
background_title_bar = """#3B5998"""
color_title_bar = """white"""
color_button_title_bar = """#dddddd"""
hover_button_title_bar = """#4267b2"""

styleSheet = """
    #titleBar{
        background: """ + background_title_bar + """;""" + """
        QLabel{
            color: """ + color_title_bar + """;""" + """
        }
    }

    QLabel{
        color: """ + color_title_bar + """;""" + """
    }

    QPushButton{
        border-style: outset;
        border-width: 0px;
        border-color: transparent;
        color: """ + color_button_title_bar + """;""" + """
        font: bold 14px;
    }

    QPushButton::hover{
        background: """ + hover_button_title_bar + """;""" + """
    }

    QPushButton#close::hover{
        background: red;
    }

    #content{
        background: #e9ebee;
    }

    #main{
        background: #3a3a3a;
    }

    QMenuBar{
        background: transparent;
        color: #111111;
    }

    QMenuBar::item:selected{
        background: #bbbbbb;
    }

    QMenu{
        background: #f6f7f9;
        color: #222222;
    }

    QMenu::item:selected{
        background: #bbbbbb;
    }
"""