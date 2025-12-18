## 1. Issue Type
- **SPEAKER_FOCUS**

## 2. Expected Behavior
The system should maintain focus on the primary speaker and not reset the conversation due to background speech.

## 3. Actual Behavior
The system reset the conversation and interrupted during a thinking pause.

## 4. Reproduction Steps
1. Start a voice conversation.
2. Pause briefly while thinking.
3. Introduce background speech.
4. Observe conversation reset.

## 5. Conversation Evidence (Sanitized)
```text
U: 我刚才在跟你说那个问题，其实我还没说完……
(background: someone nearby speaks)
A: 好的，我们重新开始。
U: 没有，我刚才只是停顿了一下，我还在想。
A: 抱歉，请继续。

6. Observed Signals

background_speech_or_noise: true

thinking_pause_markers: true

interruption_markers: true

7. Severity

 1 - [x] 2 - [ ] 3 - [ ] 4

8. Consent & Responsibility

Submitted content is sanitized or submitted at the reporter’s responsibility.
