<template>
    <section class="section hero">
        <div class="container" id="contactContainer">
            <h3 class="subtitle is-3">Contact Me</h3>
            <form name="contactForm" netlify>
                <div class="columns is-centered">
                    <div class="column">
                        <div class="field animated fadeInUp delay-1s" id="nameField" hidden>
                            <label class="label">Name</label>
                            <div class="control">
                                <input type="text" class="input" placeholder="Enter name" id="nameInput">
                            </div>
                        </div>
                    </div>
                    <div class="column">
                        <div class="field animated fadeInUp delay-1s" id="emailField" hidden>
                            <label class="label">Email</label>
                            <div class="control">
                                <input type="text" class="input" placeholder="Enter email" id="emailInput">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="columns is-centered">
                    <div class="column">
                        <div class="field animated fadeInUp delay-1s" id="messageField" hidden>
                            <label class="label">Message</label>
                            <div class="control">
                                <textarea cols="30" rows="10" class="textarea" id="messageTextarea">Enter a message</textarea>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="columns is-centered">
                    <div class="column is-one-third">
                        <div class="field animated fadeInUp delay-2s" id="submitButtonField" hidden>
                            <div class="control">
                                <button class="button is-rounded" id="submitButton">Submit</button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Contact',
    methods: {
        handleScroll: function() {
            
            var rect = document.getElementById('contactContainer').getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                document.getElementById('nameField').removeAttribute('hidden');
                document.getElementById('emailField').removeAttribute('hidden');
                document.getElementById('messageField').removeAttribute('hidden');
                document.getElementById('submitButtonField').removeAttribute('hidden');
            }

        },
        handleSubmitButtonClick: function() {
            var nameInput = document.getElementById('nameInput');
            var emailInput = document.getElementById('emailInput');
            var messageTextarea = document.getElementById('messageTextarea');
            if (!nameInput.value) {
                alert('Enter a name');
                return;
            }
            if (!emailInput.value) {
                alert('Enter an email');
                return;
            }
            if (!messageTextarea.value) {
                alert('Enter a message');
                return;
            }
        }
    },
    mounted() {
        document.addEventListener('scroll', this.handleScroll);
        //document.getElementById('submitButton').addEventListener('click', this.handleSubmitButtonClick);
    }
};
</script>

<style scoped>
@media only screen and (max-width: 769px) {
    button {
        margin-left: 36%;
    }
}
@media only screen and (min-width: 770px) {
    button {
        margin-left: 20%;
    }
}
</style>

