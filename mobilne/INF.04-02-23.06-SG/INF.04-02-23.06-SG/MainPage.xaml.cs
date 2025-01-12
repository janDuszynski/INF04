namespace INF._04_02_23._06_SG
{
    public partial class MainPage : ContentPage
    {
        public string[] text = {"Dzień dobry", "Good morning", "Buenos dias"};
        public int Selected = 0;

        public MainPage()
        {
            InitializeComponent();
        }

        private void Slider_ValueChanged(object sender, ValueChangedEventArgs e)
        {
            if (e.NewValue != null)
            {
                
                var value = Math.Round(e.NewValue, 0);
                DisplaySize.Text = $"Rozmiar: {value.ToString()}";
                TextToChange.FontSize = value;
            }
            
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            Selected += 1;
            if (Selected == 3) Selected = 0;

            TextToChange.Text = text[Selected];
        }
    }

}
