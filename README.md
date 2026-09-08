# Spotify Desktop Application

A lightweight Python desktop application that integrates with Spotify to display the currently playing track and provide quick playback controls.

The application uses the Spotify Web API through **Spotipy**, with a **Tkinter** graphical interface. It authenticates the user through Spotify OAuth, displays the current track and artists, automatically refreshes the displayed information, and provides a button for skipping to the next song.

---

## Features

* **Currently Playing Track**

  * Displays the name of the currently playing song.
  * Displays the artists associated with the track.

* **Skip Song**

  * Skip the currently playing song using Spotify's playback API.

* 🔐 **Spotify OAuth Authentication**

  * Authenticates with Spotify using Spotipy's OAuth implementation.
  * Uses environment variables for Spotify application credentials.

* 🔄 **Automatic Track Updates**

  * Periodically checks Spotify for the currently playing track.
  * Updates the desktop interface when the track changes.

* 🖥️ **Desktop GUI**

  * Built using Python's Tkinter library.
  * Displays track information and playback controls in a compact window.

## How It Works

The application follows a simple flow:

```text
┌─────────────────────┐
│      main.py        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Spotify OAuth Login │
│    via Spotipy      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Tkinter GUI      │
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌──────────┐ ┌──────────────┐
│ Current  │ │  Skip Song   │
│  Track   │ │   Control    │
└────┬─────┘ └──────┬───────┘
     │              │
     └──────┬───────┘
            ▼
    ┌─────────────────┐
    │  Spotify Web    │
    │      API        │
    └─────────────────┘
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DazzaGitHubAccount/Spotify-Desktop-Application.git

cd Spotify-Desktop-Application
```

### 2. Install Python

Make sure Python is installed on your system.

You can verify your installation with:

```bash
python --version
```

---

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install spotipy python-dotenv requests
```

---

### 4. Create a Spotify Developer Application

Create an application through the Spotify Developer Dashboard.

You will need:

* Client ID
* Client Secret
* Redirect URI

The redirect URI must match the URI configured for your Spotify application.

---

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=your_redirect_uri
```

Do **not** commit your `.env` file or Spotify credentials to GitHub.

---

## Running the Application

Run:

```bash
python main.py
```

On the first run, Spotipy will handle the Spotify authentication process.

After authentication, the desktop interface will open.

---

## Required Spotify Permissions

The application requests permissions for:

```text
user-read-playback-state
user-modify-playback-state
```

These permissions allow the application to:

* Read the currently playing track.
* Control playback, including skipping tracks.

---

## License

This project is a personal learning project and is not affiliated with or endorsed by Spotify.

Spotify and its associated trademarks belong to Spotify AB.

```
```
