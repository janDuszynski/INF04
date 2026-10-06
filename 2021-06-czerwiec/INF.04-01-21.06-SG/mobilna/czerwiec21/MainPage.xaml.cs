namespace czerwiec21
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            string email = email_entry.Text ?? "";
            string password = password_entry.Text ?? "";
            string repeatPassword = repeat_password_entry.Text ?? "";

            if (!email.Contains('@'))
            {
                message_label.Text = "Nieprawidłowy adres e-mail";
            }
            else if (password != repeatPassword)
            {
                message_label.Text = "Hasła się różnią";
            }
            else
            {
                message_label.Text = $"Witaj {email}";
            }
        }
    }
}
