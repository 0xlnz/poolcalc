window.addEventListener('load', () => {
    const darkSwitch = document.getElementById('darkSwitch');
    initTheme(); // if user has already selected a theme, initialize it

    darkSwitch.addEventListener('change', () => {
        resetTheme(); // update body classes whenever the switch is toggled
    });

    function initTheme() {
        const darkThemeSelected = localStorage.getItem('darkSwitch') !== null && localStorage.getItem('darkSwitch') === 'dark';
        darkSwitch.checked = darkThemeSelected;
        darkThemeSelected ? document.body.setAttribute('class', 'dark-mode') : document.body.removeAttribute('class');
    };

    function resetTheme() {
        if(darkSwitch.checked) {
            document.body.setAttribute('class', 'dark-mode');
            localStorage.setItem('darkSwitch', 'dark');
        } else {
            document.body.removeAttribute('class');
            localStorage.removeItem('darkSwitch');
        }
    };
});