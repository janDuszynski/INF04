namespace styczen22
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

            if (!email.Contains("@"))
            {
                message_label.Text = "Nieprawidłowy adres e-mail";
            }
            else if (password_entry.Text != repeat_password_entry.Text)
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
