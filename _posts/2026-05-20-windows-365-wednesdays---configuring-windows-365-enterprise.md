---
layout: post
title: "Windows 365 Wednesdays - Configuring Windows 365 Enterprise"
author: jeroen
categories: [Podcast]
tags: [intune, modern-workplace]
image: ""
date: 2026-05-20 06:26:53 +0000
audio: "https://substack-post-media.s3.amazonaws.com/public/images/ad724d06-e126-48c2-9e5d-1e0977092f08_2000x1125.jpeg"
duration: ""
episode: ""
link: "https://www.burgerhout.org/p/windows-365-wednesdays-configuring-windows-365-enterprise"
description: "



In the first part of this series, we covered the basics of Windows 365, licensing, and the differences between Business and Enterprise.
Now it’s time to actually build a Windows 365 Enterprise..."
---

<audio controls style="width:100%"><source src="https://substack-post-media.s3.amazonaws.com/public/images/ad724d06-e126-48c2-9e5d-1e0977092f08_2000x1125.jpeg" type="audio/mpeg"></audio>


<div class="captioned-image-container"><figure><a class="image-link image2" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!QSu1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!QSu1!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 424w, https://substackcdn.com/image/fetch/$s_!QSu1!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 848w, https://substackcdn.com/image/fetch/$s_!QSu1!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!QSu1!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!QSu1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":null,"width":null,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":false,"topImage":true,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!QSu1!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 424w, https://substackcdn.com/image/fetch/$s_!QSu1!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 848w, https://substackcdn.com/image/fetch/$s_!QSu1!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!QSu1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f24d69d-71a5-403e-9d34-cc80f41a500e_2000x1125.jpeg 1456w" sizes="100vw" fetchpriority="high"></source></picture><div></div>
</div></a></figure></div>
<p>In the <a href="https://burgerhou.tj/iigegb?ref=burgerhout.org">first part</a> of this series, we covered the basics of Windows 365, licensing, and the differences between Business and Enterprise.</p>
<p>Now it’s time to actually build a Windows 365 Enterprise environment.</p>
<p>Unlike Windows 365 Business, the Enterprise edition gives administrators much more control over:</p>
<ul>
<li><p>networking</p></li>
<li><p>identity</p></li>
<li><p>management</p></li>
<li><p>security</p></li>
<li><p>provisioning</p></li>
</ul>
<p>The tradeoff is simple:<br>more flexibility also means more configuration.</p>
<p>In this post, I’ll walk through the core components required to successfully deploy Windows 365 Enterprise using Microsoft Intune.</p>
<p>I’ll cover:</p>
<ul>
<li><p>prerequisites</p></li>
<li><p>networking</p></li>
<li><p>Azure Network Connection</p></li>
<li><p>provisioning policies</p></li>
<li><p>images</p></li>
<li><p>assignments</p></li>
<li><p>common deployment mistakes</p></li>
</ul>
<h3>Understanding the architecture</h3>
<p>A Windows 365 Enterprise deployment consists of several components working together:</p>
<ul>
<li><p>Microsoft Intune</p></li>
<li><p>Microsoft Entra ID</p></li>
<li><p>Windows 365 licensing</p></li>
<li><p>provisioning policies</p></li>
<li><p>Cloud PC images</p></li>
</ul>
<p>At a high level, the provisioning flow looks like this:</p>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!sMnf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!sMnf!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 424w, https://substackcdn.com/image/fetch/$s_!sMnf!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 848w, https://substackcdn.com/image/fetch/$s_!sMnf!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 1272w, https://substackcdn.com/image/fetch/$s_!sMnf!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!sMnf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg" width="345" height="918" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/fd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":918,"width":345,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!sMnf!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 424w, https://substackcdn.com/image/fetch/$s_!sMnf!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 848w, https://substackcdn.com/image/fetch/$s_!sMnf!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 1272w, https://substackcdn.com/image/fetch/$s_!sMnf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd2fbc3b-3abe-428f-8f04-d7b277a7e6f6_345x918.svg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a></figure></div>
<p>From an administrator perspective, most of the work happens before the first Cloud PC is created.</p>
<p>Good preparation prevents most provisioning failures later on.</p>
<h3>Prerequisites</h3>
<p>Before configuring anything, validate the following requirements.</p>
<h4><em>Required components</em></h4>
<p>At minimum you need:</p>
<ul>
<li><p>a Windows 365 Enterprise license</p></li>
<li><p>Microsoft Intune</p></li>
<li><p>Microsoft Entra ID</p></li>
<li><p>supported networking</p></li>
<li><p>administrative permissions</p></li>
</ul>
<p>In most modern environments, this is already enough to start deploying Cloud PCs relatively quickly.</p>
<p>One of the biggest advantages of Windows 365 Enterprise is that administrators can keep the deployment relatively straightforward while still maintaining enterprise-grade management capabilities.</p>
<div class="callout-block" data-callout="true"><p>💡Windows 365 Enterprise also supports more advanced networking scenarios through Azure Network Connection (ANC), allowing Cloud PCs to connect directly to Azure virtual networks and internal resources. While powerful, ANC also introduces additional dependencies around networking, DNS, and connectivity. For this blog series, we’ll focus on the simpler and more modern deployment approach first.</p></div>
<h3>Provisioning policies explained</h3>
<p>Provisioning policies define how Cloud PCs are created. Think of them as the deployment blueprint. A provisioning policy controls:</p>
<ul>
<li><p>region</p></li>
<li><p>image</p></li>
<li><p>join type</p></li>
<li><p>language settings</p></li>
<li><p>assignments</p></li>
</ul>
<p>Without a provisioning policy, no Cloud PCs will be created.</p>
<h4><em>Creating a provisioning policy</em></h4>
<ol>
<li><p>Inside <strong>Intune</strong>, navigate to -> <strong>Devices</strong> -> <strong>Manage Windows 365 Cloud PCs</strong> -> <strong>Provision Cloud PCs</strong></p></li>
<li><p>Click on <strong>Create policy</strong></p></li>
<li><p>In the <strong>Name</strong> field, give the policy the desired name</p></li>
<li><p>Choose at <strong>Experience</strong>, in this example, for <strong>Access a full Cloud PC Desktop</strong></p></li>
<li><p>At <strong>License type</strong>, click Enterprise.</p></li>
<li><p>At <strong>Join type</strong>, click <strong>Microsoft Entra Join</strong></p></li>
<li><p>At <strong>Network</strong>, click <strong>Microsoft hosted network</strong></p></li>
<li><p>Choose your <strong>Geography and regions</strong></p></li>
<li><p>Check the box for <strong>Microsoft Entra Single sign-on</strong></p></li>
<li><p>Click <strong>Next</strong></p></li>
<li><p>Choose an <strong>Image type</strong></p></li>
<li><p>Choose the <strong>Language & Region</strong></p></li>
<li><p>Create a <strong>Device name template</strong></p></li>
<li><p>Optional: Link an Autopilot Device preparation policy</p></li>
<li><p>At <strong>Additional Services</strong>, I choose for Autopatch, because I have that running in this tenant.</p></li>
<li><p>Click <strong>Next</strong></p></li>
<li><p>Click <strong>Next</strong>.</p></li>
<li><p>Assign the policy to the group of licensed users</p></li>
<li><p>Review the settings and click <strong>Next</strong></p></li>
</ol>
<p>For most deployments, the default Microsoft-hosted networking configuration is more than sufficient and keeps the deployment process much simpler.</p>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!Rj2h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!Rj2h!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 424w, https://substackcdn.com/image/fetch/$s_!Rj2h!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 848w, https://substackcdn.com/image/fetch/$s_!Rj2h!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!Rj2h!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!Rj2h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg" width="792" height="1192" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":1192,"width":792,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!Rj2h!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 424w, https://substackcdn.com/image/fetch/$s_!Rj2h!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 848w, https://substackcdn.com/image/fetch/$s_!Rj2h!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!Rj2h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72284667-774e-4ad8-b5c5-ff0b6f913955_792x1192.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a></figure></div>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!xON9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!xON9!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 424w, https://substackcdn.com/image/fetch/$s_!xON9!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 848w, https://substackcdn.com/image/fetch/$s_!xON9!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!xON9!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!xON9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg" width="801" height="1042" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/d315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":1042,"width":801,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!xON9!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 424w, https://substackcdn.com/image/fetch/$s_!xON9!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 848w, https://substackcdn.com/image/fetch/$s_!xON9!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!xON9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd315b85a-3a68-4f1c-8f13-d468c64c44de_801x1042.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a></figure></div>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!tCIH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!tCIH!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 424w, https://substackcdn.com/image/fetch/$s_!tCIH!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 848w, https://substackcdn.com/image/fetch/$s_!tCIH!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!tCIH!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!tCIH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg" width="777" height="1264" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/c2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":1264,"width":777,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!tCIH!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 424w, https://substackcdn.com/image/fetch/$s_!tCIH!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 848w, https://substackcdn.com/image/fetch/$s_!tCIH!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!tCIH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2f260a3-4ae9-4ac8-af1b-5cb882495bf2_777x1264.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a></figure></div>
<h3>Selecting images</h3>
<p>Windows 365 supports multiple image options.</p>
<h4><em>Gallery images</em></h4>
<p>Microsoft provides prebuilt images including:</p>
<ul>
<li><p>Windows 11</p></li>
<li><p>Microsoft 365 Apps</p></li>
<li><p>Teams optimization</p></li>
</ul>
<p>These are the easiest to maintain and are ideal for most deployments.</p>
<h4><em>Custom images</em></h4>
<p>Organizations can also deploy their own images.<br>This is useful for:</p>
<ul>
<li><p>preinstalled applications</p></li>
<li><p>hardened configurations</p></li>
<li><p>specialized workloads</p></li>
<li><p>legacy software requirements</p></li>
</ul>
<p>My recommendation:<br>Start with gallery images unless there is a strong business reason not to.</p>
<p>Custom images increase operational overhead quickly.</p>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!rUDM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!rUDM!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 424w, https://substackcdn.com/image/fetch/$s_!rUDM!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 848w, https://substackcdn.com/image/fetch/$s_!rUDM!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!rUDM!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!rUDM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg" width="797" height="396" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/c7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":396,"width":797,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!rUDM!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 424w, https://substackcdn.com/image/fetch/$s_!rUDM!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 848w, https://substackcdn.com/image/fetch/$s_!rUDM!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!rUDM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c8355a-a18b-4091-b1d4-0a5bcbf13ec6_797x396.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a></figure></div>
<h3>Assigning users</h3>
<p>Once the provisioning policy is configured, assignments determine who receives a Cloud PC. Typically this is done using:</p>
<ul>
<li><p>Entra ID groups</p></li>
<li><p>dynamic groups</p></li>
<li><p>department-based assignments</p></li>
</ul>
<p>As soon as:</p>
<ul>
<li><p>the user has a valid license</p></li>
<li><p>and receives the provisioning policy</p></li>
</ul>
<p>the Cloud PC deployment starts automatically.</p>
<p>Provisioning usually takes between 20 minutes to several hours, depending on:</p>
<ul>
<li><p>image type</p></li>
<li><p>deployment complexity</p></li>
<li><p>assigned applications and policies</p></li>
</ul>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!Hy5X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!Hy5X!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 424w, https://substackcdn.com/image/fetch/$s_!Hy5X!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 848w, https://substackcdn.com/image/fetch/$s_!Hy5X!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!Hy5X!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!Hy5X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg" width="793" height="505" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":505,"width":793,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Configuring Windows 365 Enterprise","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" title="Windows 365 Wednesdays - Configuring Windows 365 Enterprise" srcset="https://substackcdn.com/image/fetch/$s_!Hy5X!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 424w, https://substackcdn.com/image/fetch/$s_!Hy5X!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 848w, https://substackcdn.com/image/fetch/$s_!Hy5X!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!Hy5X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7429fadb-54bf-4e10-949a-e29415721208_793x505.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a></figure></div>
<h3>Intune enrollment</h3>
<p>After provisioning completes, the Cloud PC automatically enrolls into Intune. From there, it behaves almost like a normal Windows endpoint.</p>
<p>Administrators can deploy:</p>
<ul>
<li><p>compliance policies</p></li>
<li><p>configuration profiles</p></li>
<li><p>applications</p></li>
<li><p>security baselines</p></li>
<li><p>Defender policies</p></li>
<li><p>update rings / Autopatch</p></li>
</ul>
<p>This is where Windows 365 becomes especially powerful for organizations already using Intune extensively.</p>
<p>The management experience is very familiar for endpoint administrators because most existing Intune workflows continue to work exactly the same.</p>
<h3>Common deployment mistakes</h3>
<p>I’ve seen the same problems come up again and again during deployments in recent months. I'll mention a few from my experiences.</p>
<h4><em>Overcomplicating the first rollout</em></h4>
<p>Keep the initial deployment simple.</p>
<p>Do not immediately introduce:</p>
<ul>
<li><p>custom images</p></li>
<li><p>dozens of applications</p></li>
<li><p>complex security baselines</p></li>
<li><p>advanced networking requirements</p></li>
</ul>
<p>Validate the platform first.</p>
<h4><em>Deploying too many applications during provisioning</em></h4>
<p>Heavy application deployments can slow down the user onboarding experience significantly.</p>
<p>Especially large Win32 apps may delay the first login experience.</p>
<h4><em>Using custom images too early</em></h4>
<p>Custom images sound attractive, but they also become operationally expensive.<br>Many organizations can achieve the same result using:</p>
<ul>
<li><p>Intune</p></li>
<li><p>application deployment</p></li>
<li><p>configuration profiles</p></li>
</ul>
<p>without maintaining image lifecycles manually.</p>
<h4><em>Treating Cloud PCs differently from endpoints</em></h4>
<p>A Cloud PC is still a Windows endpoint. Many existing Intune and security principles still apply.</p>
<h3>Final Thoughts</h3>
<p>Windows 365 Enterprise is relatively straightforward once the foundational components are designed correctly.<br>Most deployment challenges are not caused by Windows 365 itself, but by:</p>
<ul>
<li><p>unnecessary complexity</p></li>
<li><p>overengineering</p></li>
<li><p>or introducing advanced scenarios too early</p></li>
</ul>
<p>My recommendation is always: start simple, validate the platform, and scale gradually.</p>
<p>In the next part of this series, we’ll take a closer look at <a href="https://burgerhou.tj/wg8bws?ref=burgerhout.org">Cloud PC settings</a>, management capabilities, and the options administrators have after deployment.</p>
<p>That is it for now. Until next time. 👋</p>


[Listen on Substack](https://www.burgerhout.org/p/windows-365-wednesdays-configuring-windows-365-enterprise)
