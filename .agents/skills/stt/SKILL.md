---
name: stt
description: Transcribe audio files using local whisper and return the extracted text. ALWAYS reply with the full transcription when using this skill.
version: 1.0.0
author: IdrisBot
tags:
  - audio
  - transcription
  - whisper
  - speech-to-text
triggers:
  - "transcribe audio"
  - "speech to text"
  - "stt"
  - "whisper"
  - "convert audio to text"
  - "what did I say"
  - "what's in this audio"
---

# STT — Speech-to-Text Transcription

Transcribe audio files using local whisper and **ALWAYS** reply with the extracted text.

## The One Rule

**When you use this skill, you MUST include the full transcription in your response.**

No black-boxing. No summarizing. No "I transcribed it and here's what they said." The actual words, in full.

Jae's directive: "If you use stt always reply with what you extracted."

## Usage

### Input
- Audio file path (m4a, mp3, wav, etc.)
- Optional: model size ('base', 'small', 'medium')

### Output
- Full transcription text
- MUST be included in the reply to the user

### Run Pattern

```bash
# Convert to mp3 first if needed (m4a, etc.)
ffmpeg -i input.m4a -f mp3 -ar 16000 -ac 1 /tmp/audio.mp3 -y 2>/dev/null

# Transcribe with local whisper
uv run --with openai-whisper python3 -c "
import whisper
model = whisper.load_model('base')
result = model.transcribe('/tmp/audio.mp3')
print(result['text'])
"
```

### Complete Example

```bash
# One-shot transcription
cd /home/jaewilson07/GitHub/libraries/cboti && uv run --no-project python3 << 'PYEOF'
import subprocess
import sys

audio_path = "/path/to/audio.m4a"

# Convert to mp3
subprocess.run([
    "ffmpeg", "-i", audio_path, "-f", "mp3",
    "-ar", "16000", "-ac", "1", "/tmp/audio.mp3", "-y"
], capture_output=True)

# Transcribe
subprocess.run([
    "uv", "run", "--with", "openai-whisper", "python3", "-c",
    "import whisper; model = whisper.load_model('base'); result = model.transcribe('/tmp/audio.mp3'); print(result['text'])"
], check=True)
PYEOF
```

## Model Selection

- `base` — Fast, good for short clips (< 30 sec). Default.
- `small` — Better accuracy, still fast. Good for 1-2 min clips.
- `medium` — Best accuracy, slower. Use for longer audio.

## Why This Skill Exists

Before this skill, I would transcribe audio and sometimes forget to include the text in my reply. This skill bakes the rule into the tool: if you invoke it, you share the output.

The skill is the enforcement mechanism. No more "I transcribed it" without the actual words.

## Integration Notes

- Works with Letta's inbound Slack audio attachments
- Audio files land in `~/.letta/channels/slack/inbound/idrisbot/`
- File naming: `{message_id}-{timestamp}-{name}.m4a`
- Use `ffmpeg` to convert to mp3 before whisper (whisper handles mp3 best)

## Example Session

**User sends audio clip**

**Agent:**
1. Receives audio file path from Slack attachment
2. Converts to mp3 with ffmpeg
3. Transcribes with local whisper
4. Replies with the full transcription text

**Correct reply:**
> Here's what you said:
> 
> "Hey, Idris, take each of these roles and block 20 minutes on my calendar..."

**Incorrect reply:**
> I transcribed your audio. You want me to block calendar time for skills.

The second reply is WRONG. The first reply is RIGHT. This skill enforces the right behavior.
