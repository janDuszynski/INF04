namespace czerwiec25
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();

            MainPage = new AppShell();
        }

        protected override Window CreateWindow(IActivationState? activationState)
        {
            Window window = base.CreateWindow(activationState);
            window.Title = "Wzornik kolorów RGB. Wykonał 00000000000";
            return window;
        }
    }
}
