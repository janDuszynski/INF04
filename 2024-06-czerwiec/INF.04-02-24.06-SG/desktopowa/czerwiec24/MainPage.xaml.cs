namespace czerwiec24
{
    public partial class MainPage : ContentPage
    {
        public string[] DataArray;
        public int AlbumCount = 0;
        public int SelectedAlbum = 0;

        public MainPage()
        {
            LoadDataFromFile();
            InitializeComponent();
            
        }

        private async void LoadDataFromFile()
        {
            string fileName = "Data.txt"; 

            try
            {
                using var stream = await FileSystem.OpenAppPackageFileAsync(fileName);
                using var reader = new StreamReader(stream);

                string content = await reader.ReadToEndAsync();
                DataArray = content.Split(new[] { '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);

                AlbumCount = DataArray.Length / 5;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Błąd podczas wczytywania pliku: {ex.Message}");
            }
        }

        private void downloadButton_Clicked(object sender, EventArgs e)
        {
            int currentCount = int.Parse(DataArray[SelectedAlbum + 4]);
            currentCount += 1;
            DataArray[SelectedAlbum + 4] = currentCount.ToString();
            albumDownloadCount.Text = DataArray[SelectedAlbum + 4];
        }


        private void Button_Clicked(object sender, EventArgs e)
        {
            SelectedAlbum += 5;
            if (SelectedAlbum == DataArray.Length)
                    SelectedAlbum = 0;

            albumArtist.Text = DataArray[SelectedAlbum];
            albumTitle.Text = DataArray[SelectedAlbum + 1];
            albumTracksCount.Text = DataArray[SelectedAlbum + 2];
            albumYear.Text = DataArray[SelectedAlbum + 3];
            albumDownloadCount.Text = DataArray[SelectedAlbum + 4].ToString();
        }
    }
}
