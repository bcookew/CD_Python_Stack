
async function call_github() {
    var response = await fetch("https://api.github.com/users/bcookew");
    var profile = await response.json();
    console.log(profile);
    profilePhoto = document.getElementById("profilePhoto")
    profilePhoto.src = profile.avatar_url
}
