// dateUtils.js

// Format the date
const formatDate = (dateString) => {
    const dateObject = new Date(dateString);
    const currentDate = new Date();

    // Check if the date is within the current day (0-24h)
    if (
        dateObject.getDate() === currentDate.getDate() &&
        dateObject.getMonth() === currentDate.getMonth() &&
        dateObject.getFullYear() === currentDate.getFullYear()
    ) {
        // Format time in 12-hour AM/PM format
        let hours = dateObject.getHours();
        const amPm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12 || 12;
        const minutes = dateObject.getMinutes().toString().padStart(2, '0');
        return `${hours}:${minutes} ${amPm}`;
    }

    // Check if the date was yesterday
    const yesterday = new Date(currentDate);
    yesterday.setDate(currentDate.getDate() - 1);
    if (
        dateObject.getDate() === yesterday.getDate() &&
        dateObject.getMonth() === yesterday.getMonth() &&
        dateObject.getFullYear() === yesterday.getFullYear()
    ) {
        return 'Yesterday';
    }

    // Check if the date was within the last week
    const oneWeekAgo = new Date(currentDate);
    oneWeekAgo.setDate(currentDate.getDate() - 7);
    if (dateObject > oneWeekAgo) {
        // Output the day name
        const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        return daysOfWeek[dateObject.getDay()];
    }

    // If none of the above conditions match, return the year-month-day format
    return `${dateObject.getFullYear()}-${(dateObject.getMonth() + 1).toString().padStart(2, '0')}-${dateObject.getDate().toString().padStart(2, '0')}`;
};

// Export the formatDate function
export {formatDate};