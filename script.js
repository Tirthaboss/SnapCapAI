// Function to redirect user to another page
function redirectToPage(url) {
    // Check if the user has permission to access the page
    if (hasPermission()) {
        // Redirect the user to the page
        window.location.href = url;
    } else {
        // Display an error message or handle the lack of permission
        alert("You do not have permission to access this page.");
        // Optionally, redirect to a different page or display a message
        window.location.href ="https://snapcapai.sreamlit.app"                   
    }
}

                                               
function hasPermission() {
                                                              
                                                                
    const userRole = localStorage.getItem("https://snapcapai.sreamlit.app";
    }
}

// Function to check if the user has permission
function hasPermission() {
    // Replace this with your actual permission checking logic
    // For example, you might check a user's role or permissions
    const userRole = localStorage.getItem("userRole");
    return userRole === "admin" || userRole === "moderator";
}

                                    
document.addEventListener("// Redirect to the page on page load
document.addEventListener("DOMContentLoaded", function() {
    const redirectUrl = "https://snapcapai.sreamlit.app";
    redirectToPage(redirectUrl);
});