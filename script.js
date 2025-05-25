const hasPermission = async () => {
    const userRole = localStorage.getItem("userRole");
    return userRole === "admin" || userRole === "moderator";
};

const redirectToPage = async (url) => {
    if (await hasPermission()) {
        window.location.href = url;
    } else {
        alert("You do not have permission to access this page.");
    }
};

// Example usage:
document.getElementById("redirectButton").addEventListener("click", () => {
    redirectToPage("https://example.com/protected-page");
});