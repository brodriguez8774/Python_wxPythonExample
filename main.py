"""
Test of how wxPython's interface works.
"""

import wx


class WindowFrame(wx.Frame):
    """
    Window Frame object. Contains general layout.
    """
    def __init__(self, *args, **kwargs):
        """
        Object initialization.
        """
        super(WindowFrame, self).__init__(*args, **kwargs)

        self.user_input_group = None

        self.initialize_layout()
        self.SetMinSize((300, 200))  # Set minimum size to be default window size.
        self.Center()   # Center window on screen.
        self.Show()     # Display window.

    def initialize_layout(self):
        """
        Initializes overall layout of program.
        """
        # Create row groups.
        top_row_sizer = self.create_gui_top_row()
        mid_row_sizer = self.create_gui_middle_row()
        bot_row_sizer = self.create_gui_bottom_row()

        # Create window sizer.
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        form_sizer.Add(top_row_sizer, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 20)
        form_sizer.Add(mid_row_sizer, 1, wx.EXPAND | wx.RIGHT | wx.LEFT, 20)
        form_sizer.Add(bot_row_sizer, 1, wx.EXPAND | wx.RIGHT | wx.BOTTOM | wx.LEFT, 20)

        # Initialize form settings.
        self.SetAutoLayout(True)
        self.SetSizer(form_sizer)
        self.Layout()

    def create_gui_top_row(self):
        """
        Top row of GUI.
        """
        # Create group panel.
        panel = wx.Panel(self)

        # Create group sizer.
        col_sizer = wx.BoxSizer(wx.HORIZONTAL)
        col_sizer.AddStretchSpacer(1)

        # Create Title fields.
        title = wx.StaticText(panel, label='wxPython Test', style=wx.ALIGN_CENTER)
        title.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        col_sizer.Add(title, 1, wx.ALIGN_CENTER)
        col_sizer.AddStretchSpacer(1)

        panel.SetSizer(col_sizer)
        return panel

    def create_gui_middle_row(self):
        """
        Middle row of GUI.
        """
        # Create group panel.
        panel = wx.Panel(self)

        # Create group sizer.
        col_sizer = wx.BoxSizer(wx.HORIZONTAL)
        col_sizer.AddStretchSpacer(1)

        # Create login fields.
        self.user_input_group = self.create_user_input_fields(parent=panel)
        col_sizer.Add(self.user_input_group, 2, wx.ALIGN_CENTER)
        col_sizer.AddStretchSpacer(1)

        panel.SetSizer(col_sizer)
        return panel

    def create_user_input_fields(self, parent=None):
        """
        Create username and password fields.
        """
        # Create group panel.
        if parent is None:
            parent = self
        panel = wx.Panel(parent)

        # Create group sizer.
        row_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create username text.
        username_text = wx.StaticText(panel, label='Username', style=wx.ALIGN_CENTER)
        row_sizer.Add(username_text, 1, wx.ALIGN_CENTER)

        # Create username box.
        panel.username_input = wx.TextCtrl(panel)
        row_sizer.Add(panel.username_input, 1, wx.EXPAND | wx.ALIGN_CENTER)
        row_sizer.AddSpacer(20)

        # Create password text.
        password_text = wx.StaticText(panel, label='Password', style=wx.ALIGN_CENTER)
        row_sizer.Add(password_text, 1, wx.ALIGN_CENTER)

        # Create password box.
        panel.password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        row_sizer.Add(panel.password_input, 1, wx.EXPAND | wx.ALIGN_CENTER)

        panel.SetSizer(row_sizer)
        return panel

    def create_gui_bottom_row(self):
        """
        Bottom row of GUI.
        """
        # Create group panel.
        panel = wx.Panel(self)

        # Create group sizer.
        col_sizer = wx.BoxSizer(wx.HORIZONTAL)
        col_sizer.AddStretchSpacer(1)

        # Create Sign in button.
        sign_in_button = SignInButton(
            parent=panel,
            widget_dict={
                'window': self,
                'user_input_group': self.user_input_group,
            }
        )
        col_sizer.Add(sign_in_button, 1, wx.ALIGN_CENTER)
        col_sizer.AddStretchSpacer(1)

        panel.SetSizer(col_sizer)
        return panel


class SignInButton(wx.Button):
    """
    Sign In button object.
    """
    def __init__(self, widget_dict, *args, **kwargs):
        super(SignInButton, self).__init__(*args, **kwargs)

        self.user_status_dict = None

        # Useful groups for later manipulation.
        self.window = widget_dict['window']
        self.user_input_group = widget_dict['user_input_group']

        # Set button properties.
        self.SetLabelText('Sign In')
        self.Bind(wx.EVT_BUTTON, self.on_click)

    def on_click(self, event):
        """
        Base handling for button click.
        """
        if self.LabelText == 'Sign In':
            if self.user_input_group.username_input.GetValue().strip() is '':
                print('Please enter a username.')
            elif self.user_input_group.password_input.GetValue().strip() is '':
                print('Please enter a password.')
            else:
                self.sign_in()
        else:
            self.sign_out()

    def sign_in(self):
        """
        Sign in functionality.
        """
        print('Signed in with username of {0} and password of {1}.'.format(
            self.user_input_group.username_input.GetValue().strip(),
            self.user_input_group.password_input.GetValue().strip(),
        ))
        self.clear_input_fields()
        self.user_input_group.username_input.Disable()
        self.user_input_group.password_input.Disable()
        self.SetLabelText('Sign Out')

    def sign_out(self):
        """
        Sign out functionality.
        """
        print('Signed out.')
        self.user_input_group.username_input.Enable()
        self.user_input_group.password_input.Enable()
        self.SetLabelText('Sign In')

    def clear_input_fields(self):
        """
        Clears input fields.
        """
        self.user_input_group.username_input.SetValue('')
        self.user_input_group.password_input.SetValue('')


if __name__ == '__main__':
    print("Starting program.")

    interface = wx.App()
    WindowFrame(None, title='wxPython Test', size=(600, 400))
    interface.MainLoop()

    print("Terminating Program.")
