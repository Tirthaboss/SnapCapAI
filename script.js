const hasPermission = async () => {
    const userRole = localStorage.getItem("userRole");
    return userRole === "admin" || userRole === "moderator";
};

const redirectToPage = async (url) => {
    if (await hasPermission()) {
        window.location.href = url;
    } else {
        alert("You do not have permission to access this page.");
        window.location.href = "https://snapcapai.sreamlit.app"                            
    }
};

                                    
document.addEventListener("https://snapcapai.sreamlit.app";
    }
};

// Redirect to the page on page load
document.addEventListener("DOMContentLoaded", async () => {
    const redirectUrl = "https://snapcapai.sreamlit.app";
    await redirectToPage(redirectUrl);
});