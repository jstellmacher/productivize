import React, { useState } from "react";
import { useAppContext } from "../context/AppC";

const Profile = () => {
  const { user } = useAppContext();
  const [username, setUsername] = useState(user?.username);
  const [password, setPassword] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSaveProfile = () => {
    // Perform the PATCH request to update the username and password
    // using the `username` and `password` state values
    // You need to implement the logic for sending the request to the backend.

    // Example using fetch API:
    fetch("/users", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the backend, e.g., display a success message
      })
      .catch((error) => {
        // Handle error, e.g., display an error message
      });
  };

  const handleDeleteAccount = () => {
    // Perform the DELETE request to delete the user account
    // You need to implement the logic for sending the request to the backend.

    // Example using fetch API:
    fetch("/users", {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the backend, e.g., redirect to a login page
      })
      .catch((error) => {
        // Handle error, e.g., display an error message
      });
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-gray-400 rounded-lg shadow-md p-8 max-w-md w-full">
        <h1 className="text-2xl font-bold mb-4">Profile</h1>
        <div className="flex justify-center items-center mb-8">
          <img
            // src={user?.profilePicture}
            src={"https://picsum.photos/200/303"}
            alt="Profile"
            className="rounded-full h-50 w-50 mr-4"
          />
          <h2 className="text-xl font-semibold">{user?.name}</h2>
        </div>
        <div className="mb-8">
          <label htmlFor="username" className="block text-gray-700 font-semibold mb-2">
            Username:
          </label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={handleUsernameChange}
            className="w-full border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring focus:ring-indigo-300"
          />
        </div>
        <div className="mb-8">
          <label htmlFor="password" className="block text-gray-700 font-semibold mb-2">
            Password:
          </label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={handlePasswordChange}
            className="w-full border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring focus:ring-indigo-300"
          />
        </div>
        <div className="mb-8">
          <label htmlFor="profilePicture" className="block text-gray-700 font-semibold mb-2">
            Profile Picture:
          </label>
          <input
            type="text"
            id="profilePicture"
            defaultValue={user?.profilePicture}
            className="w-full border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring focus:ring-indigo-300"
          />
        </div>
        <div className="mb-8">
          <label htmlFor="bio" className="block text-gray-700 font-semibold mb-2">
            Bio:
          </label>
          <textarea
            id="bio"
            defaultValue={user?.bio}
            className="w-full border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring focus:ring-indigo-300"
          />
        </div>
        <button className="bg-indigo-500 text-white rounded-md px-4 py-2" onClick={handleSaveProfile}>
          Save Profile
        </button>
        <button className="bg-red-500 text-white rounded-md px-4 py-2" onClick={handleDeleteAccount}>
          Delete Account
        </button>
      </div>
    </div>
  );
};

export default Profile;
