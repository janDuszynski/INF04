namespace INF._04_01_23._01_SG
{
    public partial class MainPage : ContentPage
    {
        List<char> generatedPassword = new List<char>();
        public string password; 

        public MainPage()
        {
            InitializeComponent();
            var items = new List<string> { "Kierownik", "Starszy programista", "Młodszy programista", "Tester" };
            MyPicker.ItemsSource = items;
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            int dlugosc = Int32.Parse(PasswordLength.Text);
            const string lower = "qwertyuiopasdfghjklzxcvbnm";
            const string upper = "QWERTYUIOPASDFGHJKLZXCVBNM";
            const string digits = "0123456789";
            const string specialChars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~";

            string charPool = lower;
            if (SizeC.IsChecked)
                charPool += upper;
            if (Digits.IsChecked)
                charPool += digits;
            if (Special.IsChecked)
                charPool += specialChars;

            if (string.IsNullOrEmpty(charPool))
            {
                DisplayAlert("Błąd", "Proszę zaznaczyć przynajmniej jedną opcję.", "OK");
                return;
            }

            Random rnd = new Random();
            List<char> generatedPassword = new List<char>();

            for (int i = 0; i < dlugosc; i++)
            {
                generatedPassword.Add(charPool[rnd.Next(charPool.Length)]);
            }

            string password = new string(generatedPassword.ToArray());
            DisplayAlert("Propozycja hasła:", password, "OK");
        }

        private void Button_Clicked_1(object sender, EventArgs e)
        {
            DisplayAlert("Dane z formularza i hasło", $"Dane pracownika: {imie.Text} {nazwisko.Text}. Hasło: {password}", "OK.");
        }
    }

}
