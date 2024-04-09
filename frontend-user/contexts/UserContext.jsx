import React, { createContext, useState } from 'react';

// Create a context for user authentication and details
export const UserContext = createContext();

// UserProvider component to wrap the entire app
export const UserProvider = ({ children }) => {
    // State to manage user authentication and details
    const [user, setUser] = useState(null);

    // Function to handle user login
    const loginUser = (email, password) => {
        // Implement your authentication logic here
        // For demo purposes, let's check against the hardcoded users object
        for (const userId in users) {
            if (users[userId].email === email && users[userId].password === password) {
                setUser({ id: userId, ...users[userId] });
                return true; // Authentication successful
            }
        }
        return false; // Authentication failed
    };

    // Function to handle user logout
    const logoutUser = () => {
        setUser(null);
    };

    // Hardcoded user data for demonstration (should be replaced with your database logic)
    const users = {
        "1fPITEfiegat5F0xwXR9": {
            email: "pg@example.com",
            name: "Peter Guy",
            password: "example_password"
        },
        "w0qh0NXts4gROIOPU7Aq": {
            email: "johndoe@gmail.com",
            name: "John Doe",
            password: "12345"
        }
    };

    // Context value to be provided
    const contextValue = {
        user,
        loginUser,
        logoutUser
    };

    return (
        <UserContext.Provider value={contextValue}>
            {children}
        </UserContext.Provider>
    );
};
