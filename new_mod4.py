import subprocess
import hashlib
from datetime import datetime
import getpass
import sqlite3


class Database:
    def __init__(self, db_name='music_app.db'):
        # Connect to an SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect(db_name, timeout=10)  # Set a timeout of 10 seconds
        self.create_tables()

#class Database:
    #def __init__(self, db_name='music_app.db'):
        # Connect to an SQLite database (or create it if it doesn't exist)
       # self.conn = sqlite3.connect(db_name)
       # self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        # Create artifacts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS artifacts (
                artifact_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                content TEXT NOT NULL,
                creation_date TEXT NOT NULL,
                modification_date TEXT NOT NULL,
                checksum TEXT NOT NULL
            )
        ''')
        # Insert initial admin user
        cursor.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', ('admin', 'admin123'))
        self.conn.commit()

    def execute_query(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

    def fetch_one(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def fetch_all(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

class MusicApp:
    def __init__(self, database):
        self.database = database
        self.authenticated_users = set()  # Store authenticated users
    
    def authenticate_user(self, username, password):
        # Check if the user credentials are valid
        result = self.database.fetch_one('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        if result:
            self.authenticated_users.add(username)
            return True
        else:
            return False
    
    def is_authenticated(self, username, password):
        # Check if the user is already authenticated
        if username in self.authenticated_users:
            return True
        else:
            return self.authenticate_user(username, password)
    
    def generate_artifact_id(self):
        # Get the maximum artifact_id from the database
        result = self.database.fetch_one('SELECT MAX(artifact_id) FROM artifacts')
        max_id = result[0] if result[0] is not None else 0
        
        # Increment the maximum ID to generate a new unique ID
        return max_id + 1
            
    def encrypt_content(self, content):
        # Simple encryption by reversing the content string
        return content[::-1]
    
    def artifact_exists(self, artifact_id):
         # Check if an artifact with the given ID exists
        result = self.database.fetch_one('SELECT * FROM artifacts WHERE artifact_id = ?', (artifact_id,))
        return result is not None
    
    def store_artifact(self, artifact_id, title, artist, content, creation_date, modification_date, checksum):
        # Insert a new artifact into the database
        self.database.execute_query('''
            INSERT INTO artifacts (artifact_id, title, artist, content, creation_date, modification_date, checksum)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (artifact_id, title, artist, content, creation_date, modification_date, checksum))
    
    def update_artifact(self, artifact_id, title, artist, content, modification_date, checksum):
        # Update an existing artifact in the database
        self.database.execute_query('''
            UPDATE artifacts
            SET title = ?, artist = ?, content = ?, modification_date = ?, checksum = ?
            WHERE artifact_id = ?
        ''', (title, artist, content, modification_date, checksum, artifact_id))
    
    def delete_artifact(self, artifact_id):
        # Delete an artifact from the database
        self.database.execute_query('DELETE FROM artifacts WHERE artifact_id = ?', (artifact_id,))

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def addArtifact(self, music_app, title, artist, content):
        # Check if the user is authenticated before adding an artifact
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        # Generate a new artifact ID and create dates
        artifact_id = music_app.generate_artifact_id()
        creation_date = modification_date = datetime.now().isoformat()
        # Generate a checksum and encrypt the content
        checksum = hashlib.sha256(content.encode()).hexdigest()
        encrypted_content = music_app.encrypt_content(content)
        # Store the artifact in the database
        music_app.store_artifact(artifact_id, title, artist, encrypted_content, creation_date, modification_date, checksum)
        print("Artifact added successfully.")
    
    def updateArtifact(self, music_app, artifact_id, title, artist, content):
        # Check if the user is authenticated before updating an artifact
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
         # Check if the artifact exists
        if not music_app.artifact_exists(artifact_id):
            print("Artifact does not exist.")
            return
        # Update the modification date, checksum, and encrypted content
        modification_date = datetime.now().isoformat()
        checksum = hashlib.sha256(content.encode()).hexdigest()
        encrypted_content = music_app.encrypt_content(content)
        # Update the artifact in the database
        music_app.update_artifact(artifact_id, title, artist, encrypted_content, modification_date, checksum)
        print("Artifact updated successfully.")
    
    def deleteArtifact(self, music_app, artifact_id):
        # Check if the user is authenticated before deleting an artifact
        if not music_app.is_authenticated(self.username, self.password):
            print("User authentication failed.")
            return
        # Check if the artifact exists
        if not music_app.artifact_exists(artifact_id):
            print("Artifact does not exist.")
            return
        # Delete the artifact from the database
        music_app.delete_artifact(artifact_id)
        print("Artifact deleted successfully.")

class Administrator(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    
    def addArtifact(self, music_app, title, artist, content):
        # Only allow the admin user to add artifacts
        if self.username != 'admin':
            print("Only administrators can add artifacts.")
            return
        
        super().addArtifact(music_app, title, artist, content)
    
    def deleteArtifact(self, music_app, artifact_id):
         # Only allow the admin user to delete artifacts
        if self.username != 'admin':
            print("Only administrators can delete artifacts.")
            return
        
        super().deleteArtifact(music_app, artifact_id)

def run_tests():
    try:
        # Run Flake8 for code style checking
        print("Running Flake8:")
        flake8_process = subprocess.Popen(["flake8", "new_mod4.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        flake8_stdout, flake8_stderr = flake8_process.communicate(timeout=30)
        print(flake8_stdout)
        if flake8_stderr:
            print(flake8_stderr)

         # Run Bandit for security analysis
        print("\nRunning Bandit:")
        bandit_process = subprocess.Popen(["bandit", "-r", "new_mod4.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        bandit_stdout, bandit_stderr = bandit_process.communicate(timeout=30)
        print(bandit_stdout)
        if bandit_stderr:
            print(bandit_stderr)
        
         # Test artifact creation with checksum and encryption
        print("\nTesting Artifact Creation with Checksum and Encryption:")
        db = Database('music_app.db')
        music_app = MusicApp(db)
        admin = Administrator('admin', 'admin123')
        
        test_title = "Test Song"
        test_artist = "Test Artist"
        test_content = "This is a test content."

        # Authenticate admin user and add artifact 
        if music_app.authenticate_user(admin.username, admin.password):
            admin.addArtifact(music_app, test_title, test_artist, test_content)

            # Retrieve the artifact and verify details
            artifact_id = music_app.generate_artifact_id() - 1
            if music_app.artifact_exists(artifact_id):
                print(f"Artifact {artifact_id} exists.")

                artifact = db.fetch_one('SELECT * FROM artifacts WHERE artifact_id = ?', (artifact_id,))
                print(f"Stored artifact: {artifact}")

                expected_checksum = hashlib.sha256(test_content.encode()).hexdigest()
                print(f"Expected checksum: {expected_checksum}")
                print(f"Stored checksum: {artifact[6]}")
                print(f"Checksum verification passed: {expected_checksum == artifact[6]}")

                expected_encryption = test_content[::-1]
                print(f"Expected encrypted content: {expected_encryption}")
                print(f"Stored encrypted content: {artifact[3]}")
                print(f"Encryption verification passed: {expected_encryption == artifact[3]}")
            else:
                print("Artifact was not added.")
        else:
            print("Admin authentication failed.")
    
    except subprocess.TimeoutExpired:
        print("Timeout occurred while running tests.")

if __name__ == "__main__":
    run_tests()
    
    db = Database('music_app.db')
    music_app = MusicApp(db)
    
    # Get user input for username, password, title, and artist
    username = input("Enter username: ")
    password = getpass.getpass("Enter a password: ")
    title = input("Enter song title: ")
    artist = input("Enter artist name: ")
    
    admin = Administrator(username, password)
    # Add artifact using user-provided details
    admin.addArtifact(music_app, title, artist, "Song Content")
     # Get user input for artifact ID to delete and delete the artifact
    artifact_id_to_delete = int(input("Enter the ID of the artifact to delete: "))
    admin.deleteArtifact(music_app, artifact_id_to_delete)
