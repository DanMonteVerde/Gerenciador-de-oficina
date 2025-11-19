function generateInitials(fullName) {
    if (!fullName) return '';
    
    const names = fullName.split(' ');

    let initials = names[0].charAt(0);

 
    if (names.length > 1) {
        initials += names[names.length - 1].charAt(0);
    }
    
    return initials.toUpperCase();
}


const nameUserElement = document.getElementById('name-user');
const fullName = nameUserElement.textContent.trim(); 


const userInitials = generateInitials(fullName);


const avatarInitialsElement = document.querySelector('.profile-pic .initials');
if (avatarInitialsElement) {
    avatarInitialsElement.textContent = userInitials;
}

