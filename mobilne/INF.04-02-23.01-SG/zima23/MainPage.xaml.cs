using System.Collections.ObjectModel;

namespace zima23
{
    public partial class MainPage : ContentPage
    {
        public ObservableCollection<string> Lista = new ObservableCollection<string>();

        public MainPage()
        {
            InitializeComponent();
            ItemsList.ItemsSource = Lista;

        }

        private void Button_Clicked(object sender, EventArgs e)
        {
            if (EntryField.Text != "")
            {
                Lista.Add(EntryField.Text.ToString());
                EntryField.Text = string.Empty;
            }
        }
    }

}
