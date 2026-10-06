namespace styczen26
{
    public partial class MainPage : ContentPage
    {
        private Kosc[] kosci = new Kosc[5];
        private Image[] obrazy;

        public MainPage()
        {
            InitializeComponent();
            obrazy = new Image[] { Kosc1Image, Kosc2Image, Kosc3Image, Kosc4Image, Kosc5Image };
            for (int i = 0; i < kosci.Length; i++)
            {
                kosci[i] = new Kosc(0);
            }
        }

        private void RzutButton_Clicked(object sender, EventArgs e)
        {
            int suma = 0;
            for (int i = 0; i < kosci.Length; i++)
            {
                kosci[i].Rzut();
                obrazy[i].Source = kosci[i].NazwyPlikow[kosci[i].IdPliku];
                suma += kosci[i].LiczbaOczek;
            }
            WynikLabel.Text = suma.ToString();
        }

        private void KoscImage_Tapped(object sender, TappedEventArgs e)
        {
            int indeks = Array.IndexOf(obrazy, (Image)sender);
            if (kosci[indeks].Dostepna)
            {
                kosci[indeks].Blokuj();
                obrazy[indeks].Opacity = 0.5;
            }
            else
            {
                kosci[indeks].Dostepna = true;
                obrazy[indeks].Opacity = 1;
            }
        }
    }
}
