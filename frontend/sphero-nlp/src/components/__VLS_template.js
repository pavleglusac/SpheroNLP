import { __VLS_internalComponent, __VLS_componentsOption, __VLS_name } from './Chat.vue.js';

function __VLS_template() {
let __VLS_ctx!: InstanceType<import('./__VLS_types.js').PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {};
/* Components */
let __VLS_localComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C; } ? C : {}> & typeof __VLS_componentsOption & typeof __VLS_ctx;
let __VLS_otherComponents!: typeof __VLS_localComponents & import('./__VLS_types.js').GlobalComponents;
let __VLS_own!: import('./__VLS_types.js').SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & typeof __VLS_publicComponent & (new () => { $slots: typeof __VLS_slots; }) >;
let __VLS_components!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
/* Style Scoped */
type __VLS_StyleScopedClasses = {} &
{ 'chat-area'?: boolean; } &
{ 'message'?: boolean; } &
{ 'message-out'?: boolean; } &
{ 'message-in'?: boolean; } &
{ 'chat-inputs'?: boolean; };
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_templateComponents!: {};
{
({} as JSX.IntrinsicElements).div;
({} as JSX.IntrinsicElements).div;
(__VLS_x as JSX.IntrinsicElements)['div'] = { class: ("h-100 w-100"), };
{
({} as JSX.IntrinsicElements).div;
({} as JSX.IntrinsicElements).div;
(__VLS_x as JSX.IntrinsicElements)['div'] = { '<section': (true), ref: ("chatArea"), class: ("chat-area"), };
// @ts-ignore
(__VLS_ctx.chatArea);
// @ts-ignore
[chatArea,];
for (const [message, index] of (await import('./__VLS_types.js')).getVForSourceType(__VLS_ctx.messages)) {
// @ts-ignore
[messages,];
{
({} as JSX.IntrinsicElements).p;
({} as JSX.IntrinsicElements).p;
(__VLS_x as JSX.IntrinsicElements)['p'] = { class: ("message"), key: ((index)), };
({ 'message-out': message.author === 'you', 'message-in': message.author !== 'you' });
__VLS_styleScopedClasses = ({ 'message-out': message.author === 'you', 'message-in': message.author !== 'you' });
(message.body);
}
}
{
({} as JSX.IntrinsicElements).div;
({} as JSX.IntrinsicElements).div;
(__VLS_x as JSX.IntrinsicElements)['div'] = { id: ("invisible"), };
}
{
({} as JSX.IntrinsicElements).div;
({} as JSX.IntrinsicElements).div;
(__VLS_x as JSX.IntrinsicElements)['div'] = { style: ({}), };
{
({} as JSX.IntrinsicElements).div;
({} as JSX.IntrinsicElements).div;
(__VLS_x as JSX.IntrinsicElements)['div'] = { class: ("input-group w-75"), style: ({}), };
{
({} as JSX.IntrinsicElements).input;
({} as JSX.IntrinsicElements).input;
(__VLS_x as JSX.IntrinsicElements)['input'] = { type: ("text"), class: ("form-control rounded-extra"), placeholder: ("Type your message..."), 'aria-label': ("Chat message input"), value: ((__VLS_ctx.youMessage)), };
// @ts-ignore
[youMessage,];
}
{
({} as JSX.IntrinsicElements).button;
({} as JSX.IntrinsicElements).button;
(__VLS_x as JSX.IntrinsicElements)['button'] = { class: ("btn btn-primary rounded-end"), type: ("button"), };
type __VLS_0 = JSX.IntrinsicElements['button'];
const __VLS_1: import('./__VLS_types.js').EventObject<typeof undefined, 'click', {}, __VLS_0['onClick']> = {
click: $event => {
__VLS_ctx.sendMessage('out');
}
};
// @ts-ignore
[sendMessage,];
}
}
}
}
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
__VLS_styleScopedClasses['h-100'];
__VLS_styleScopedClasses['w-100'];
__VLS_styleScopedClasses['chat-area'];
__VLS_styleScopedClasses['message'];
__VLS_styleScopedClasses['input-group'];
__VLS_styleScopedClasses['w-75'];
__VLS_styleScopedClasses['form-control'];
__VLS_styleScopedClasses['rounded-extra'];
__VLS_styleScopedClasses['btn'];
__VLS_styleScopedClasses['btn-primary'];
__VLS_styleScopedClasses['rounded-end'];
}
declare var __VLS_slots: {};
return __VLS_slots;
}
