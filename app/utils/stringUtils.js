// stringUtils.js

// Get initials from a name
const getInitials = (name) => {
    const nameArray = name.split(" ");
    return nameArray.map(word => word[0]).join("").toUpperCase();
};

// Export the getInitials function
module.exports = getInitials;
