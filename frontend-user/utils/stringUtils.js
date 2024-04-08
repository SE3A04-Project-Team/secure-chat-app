// stringUtils.js

// Get initials from a name
const getInitials = (name) => {
    const nameArray = name.split(" ");
    return nameArray.map(word => word[0]).join("").toUpperCase();
};

// Get the first two initials from a name
const getFirstTwoInitials = (name) => {
    return name
        .split(" ") // Split the name into an array of words
        .slice(0, 2) // Take only the first two words
        .map(word => word[0]) // Get the first letter of each word
        .join("") // Concatenate the letters into a string
        .toUpperCase(); // Convert to uppercase
};

// Export the getInitials function
export {getInitials, getFirstTwoInitials};