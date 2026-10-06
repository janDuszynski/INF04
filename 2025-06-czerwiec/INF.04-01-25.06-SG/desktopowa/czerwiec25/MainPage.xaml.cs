namespace czerwiec25
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private void Slider_ValueChanged(object sender, ValueChangedEventArgs e)
        {
            int r = (int)sliderR.Value;
            int g = (int)sliderG.Value;
            int b = (int)sliderB.Value;

            labelR.Text = r.ToString();
            labelG.Text = g.ToString();
            labelB.Text = b.ToString();
            bigRectangle.Color = Color.FromRgb(r, g, b);
        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            int r = (int)sliderR.Value;
            int g = (int)sliderG.Value;
            int b = (int)sliderB.Value;

            smallRectangle.BackgroundColor = Color.FromRgb(r, g, b);
            smallRectangle.Text = $"{r}, {g}, {b}";
        }
    }
}
