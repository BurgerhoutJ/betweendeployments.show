document.addEventListener('DOMContentLoaded', function () {
    function formatTime(sec) {
        if (!isFinite(sec) || sec < 0) return '0:00';
        var m = Math.floor(sec / 60);
        var s = Math.floor(sec % 60);
        return m + ':' + (s < 10 ? '0' : '') + s;
    }

    document.querySelectorAll('.episode-player').forEach(function (wrap) {
        var audio = wrap.querySelector('audio');
        var btn = wrap.querySelector('.player-btn');
        var bar = wrap.querySelector('.player-bar');
        var fill = wrap.querySelector('.player-bar-fill');
        var elapsedEl = wrap.querySelector('.player-elapsed');
        var durationEl = wrap.querySelector('.player-duration');

        function setPlaying(playing) {
            wrap.classList.toggle('is-playing', playing);
            btn.setAttribute('aria-label', playing ? 'Pause episode' : 'Play episode');
        }

        function seek(clientX) {
            if (!audio.duration) return;
            var rect = bar.getBoundingClientRect();
            var pct = Math.min(Math.max((clientX - rect.left) / rect.width, 0), 1);
            audio.currentTime = pct * audio.duration;
        }

        btn.addEventListener('click', function () {
            if (audio.paused) {
                document.querySelectorAll('.episode-player audio').forEach(function (a) {
                    if (a !== audio) a.pause();
                });
                audio.play();
            } else {
                audio.pause();
            }
        });

        audio.addEventListener('play', function () { setPlaying(true); });
        audio.addEventListener('pause', function () { setPlaying(false); });
        audio.addEventListener('ended', function () { setPlaying(false); });

        audio.addEventListener('loadedmetadata', function () {
            if (!durationEl.textContent) durationEl.textContent = formatTime(audio.duration);
        });

        audio.addEventListener('timeupdate', function () {
            if (audio.duration) {
                var pct = (audio.currentTime / audio.duration) * 100;
                fill.style.width = pct + '%';
                bar.setAttribute('aria-valuenow', Math.round(pct));
            }
            elapsedEl.textContent = formatTime(audio.currentTime);
        });

        bar.addEventListener('click', function (e) { seek(e.clientX); });
        bar.addEventListener('keydown', function (e) {
            if (!audio.duration) return;
            if (e.key === 'ArrowRight') audio.currentTime = Math.min(audio.currentTime + 5, audio.duration);
            if (e.key === 'ArrowLeft') audio.currentTime = Math.max(audio.currentTime - 5, 0);
        });
    });
});
