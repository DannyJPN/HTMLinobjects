# oop_html.py

class HtmlElement:
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.attributes = {}
        self.children = []
        self.text = ''
        
    def add_attribute(self, key, value):
        self.attributes[key] = value

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        try:
            # Render the opening tag with attributes
            attrs = ' '.join(f'{key}="{value}"' for key, value in self.attributes.items())
            opening_tag = f'<{self.tag_name} {attrs}>' if attrs else f'<{self.tag_name}>'

            # Render the children
            children_html = self.text+'\t\n'.join(child.render() if isinstance(child, HtmlElement) else str(child) for child in self.children)

            # Render the closing tag
            closing_tag = f'</{self.tag_name}>'

            return f'{opening_tag}\n{children_html}\n{closing_tag}'
        except Exception as e:
            print(f"Error rendering HTML element: {e}")
            raise

class Input(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('input')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

class Select(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('select')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

    def add_option(self, option):
        self.add_child(option)

class Anchor(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('a')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

class Option(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('option')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

class Image(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('img')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

class Div(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('div')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

class Form(HtmlElement):
    def __init__(self, **attributes):
        super().__init__('form')
        for key, value in attributes.items():
            if key == "text":
                self.text = value
            else:
                self.add_attribute(key, value)

# Example usage
if __name__ == "__main__":
    try:
        form = Form(action="/submit", method="post")
        form.add_child(Input(type="text", name="username", placeholder="Enter your username"))
        form.add_child(Input(type="password", name="password", placeholder="Enter your password"))
        form.add_child(Input(type="submit", value="Submit"))

        select = Select(name="options")
        select.add_option(Option(value="1",text = "Option 1"))
        select.add_option(Option(value="2",text = "Option 2"))
        form.add_child(select)

        print(form.render())
    except Exception as e:
        print(f"Error in main execution: {e}")
        raise