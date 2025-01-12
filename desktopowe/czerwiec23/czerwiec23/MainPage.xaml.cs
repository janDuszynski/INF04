using System.Text.RegularExpressions;

namespace czerwiec23
{
    public partial class MainPage : ContentPage
    {
        

        public MainPage()
        {
            InitializeComponent();
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            if (PocztowkaRadio.IsChecked)
            {
                Price.Text = "Cena: 1zł";
                Zdjecie.Source = "pocztowka.png";
            }
            else if (ListaRadio.IsChecked)
            {
                Price.Text = "Cena: 1.5zł";
                Zdjecie.Source = "list.png";
            }
            else if (PaczkaRadio.IsChecked)
            {
                Price.Text = "Cena: 10zł";
                Zdjecie.Source = "paczka.png";
            }
        }

        private void Button_Clicked_1(object sender, EventArgs e)
        {
            if(Kod != null && Kod.Text.Length != 5)
{
                DisplayAlert("Message", "Niepoprawna długość kodu", "OK");
            }
            else if (Kod != null && !Regex.IsMatch(Kod.Text, @"[a-zA-Z]"))
            {
                DisplayAlert("Message", "Niepoprawny format kodu", "OK");
            }
            else
            {
                DisplayAlert("Message", "Poprawny kodzik", "OK");
            }

        }
    }

}
