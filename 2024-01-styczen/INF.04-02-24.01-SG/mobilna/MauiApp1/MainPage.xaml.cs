namespace MauiApp1
{
    public partial class MainPage : ContentPage
    {
        public string[] data = { "Pies", "Kot", "Świnka Morska" };

        public MainPage()
        {
            InitializeComponent();
            lista.ItemsSource = data;
            
        }

        private void lista_ItemTapped(object sender, ItemTappedEventArgs e)
        {
            if (e.Item == "Kot")
            {
                suwaczek.Maximum = 20;
            }
            else if (e.Item == "Pies")
            {
                suwaczek.Maximum = 18;
            }
            else if (e.Item == "Świnka Morska")
            {
                suwaczek.Maximum = 9;
            }
        }

        private void suwaczek_ValueChanged(object sender, ValueChangedEventArgs e)
        {
            int roundedValue = (int)Math.Round(e.NewValue);
            tekscik.Text = $"Ile lat? {roundedValue}";
            suwaczek.Value = roundedValue;
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            var selectedItem = lista.SelectedItem;
            string selectedItemText = selectedItem != null ? selectedItem.ToString() : "Brak wybranego elementu";

            DisplayAlert("Zapisana Wizyta", $"{imieinazwisko.Text}, {selectedItem}, {suwaczek.Value}, {cel.Text}, {timer.Time}", "OK");
        }
    }

}
