console.clear();
document.queryAll('.card').forEach(card => {
    const name = card.query('.card-info-heading').textContent,
        followButton = card.query('.card-actions-button--follow'),
        cardStatus = card.query('.card-status');
    let cardDetail, location = card.query('.card-label--location').parentElement.textContent.trim(),
        fields = card.query('.card-label--fields').parentElement.textContent.trim();

    // This code bugged for whatever reason; okay for demo purposes it's faults
    //location = location.replace(/Location:/gi, "")
    fields = fields.replace(/Fields:/gi, "");

    cardDetail = `Creative ${name} from ${location} working in fields ${fields}. Press F to follow ${name}'s work; press enter to view the creative's profile.`
    card.setAttribute('aria-label', cardDetail);

    const cardToggleCallback = instance => {
        if (followButton.classList.contains('is-following')) {
            instance.dataset.isFollowing = true;
            followButton.textContent = "Following"
            cardStatus.textContent = `Now following ${name}`;
        } else {
            instance.dataset.isFollowing = false;
            followButton.textContent = "Follow"
            cardStatus.textContent = `No longer following ${name}`;
        }
    };

    card.addEventListener('keypress', e => {
        if (document.activeElement.isEqualNode(e.target)) {
            console.log(e);
            switch (e.keyCode || e.charCode) {
            case 102:
                console.info('Following Profile')
                followButton.classList.toggle('is-following');
                cardToggleCallback(e.target);
                break;
            case 13:
                console.info('Going to profile');
                break;
            }
        }
    });

    followButton.addEventListener('click', (e) => {
        followButton.classList.toggle('is-following');
        cardToggleCallback(card);
    });

});