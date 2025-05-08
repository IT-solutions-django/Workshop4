const header = document.querySelector('header'); 
const main = document.querySelector('main'); 
const mainBg = document.querySelector('.main-bg');

setTimeout(() => {
    runHomePreloader()
}, 300);


function runHomePreloader() {
    let cont = $('h1'),
        p = 0;
    text = '';
    cont.html("");

    randomRange = 120;

    let fixedInterval = 120;

    function printHeading(onPrintComplete) {
        let timeout = fixedInterval;
        let currentIndex = 0;

        let texts = [
            'Ц',
            'ЦЕ',
            'ЦЕХ',
            'ЦЕХ №',
            'ЦЕХ №4',
        ]

        function runNextStep() {
            if (currentIndex >= texts.length) {
                setTimeout(onPrintComplete, 30);
                return;
            }

            cont.text(texts[currentIndex]);
            currentIndex++;

            setTimeout(runNextStep, fixedInterval);
        }

        runNextStep();
    }

    const waveContainer = document.querySelector('.wave-container');
    const welcomeSection = document.querySelector('.welcome-section');

    function onPrintComplete() {
        console.log('onPrintComplete');
        document.querySelector('.preloader-divider')?.classList.add('active');

        setTimeout(() => {
            main.classList.add('active');
            body.classList.add('active');

            document.querySelector('h1').classList.add('big');
            waveContainer.classList.add('active');

            setTimeout(() => {
                waveContainer.classList.add('up');
                document.querySelector('h1').classList.add('transparent');
                header.classList.add('active');
                welcomeSection.classList.add('visible');

            }, 600);

            setTimeout(() => {
                body.classList.add('scrollable');
                mainBg.classList.add('active');

                welcomeSection.classList.add('up');

            }, 700);
        }, 400);
    }
    setTimeout(() => printHeading(onPrintComplete), 150);
}