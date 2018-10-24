require('dotenv').config();
const Mastodon = require('mastodon-api');
const util = require('util');
const fs = require('mz/fs');
const exec = util.promisify(require('child_process').exec);

console.log('Mastodon bot starting..');

const M = new Mastodon({
  client_key: '',
  client_secret: '',
  access_token: '',
  timeout_ms: 60 * 1000,
  api_url: 'https://botsin.space/api/v1/',
})

// run the python script to generate new song
const cmd = 'python3 poetry_gen.py'

// call toot function
toot()
  .then(response => console.log(response))
  .catch(error => console.error(error));

// send a new toot every 24 hours
setInterval(toot, 24 * 60 * 60 * 1000);

// read python generated file
async function myReadfile() {
  try {
    const file = await fs.readFile('output.txt');
    return file.toString();
  } catch (err) {
    console.error(err)
  }
};

// send toot to the Mastodon Instance
async function toot() {
  // run the python script to generate lyrics
  await exec(cmd);
  // read the file when finished
  myReadfile()
    .then(response => sendToot(response))
    .catch(error => console.error(error));
}

function sendToot(response) {
  let lyrics = response;
  // set toot content to the generated lyrics
  const toot_msg = {
    status: lyrics
  }
  // post the toot
  M.post('statuses', toot_msg)
  return {
    success: true
  };
}