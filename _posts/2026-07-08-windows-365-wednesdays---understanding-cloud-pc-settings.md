---
layout: post
title: "Windows 365 Wednesdays - Understanding Cloud PC Settings"
author: jeroen
categories: [Podcast]
tags: [intune, modern-workplace]
image: ""
date: 2026-07-08 09:29:46 +0000
audio: "https://substack-post-media.s3.amazonaws.com/public/images/7bdfe9c9-6b7b-40eb-b072-884e154a05f5_2000x1125.jpeg"
duration: ""
episode: ""
link: "https://www.burgerhout.org/p/windows-365-wednesdays-understanding-cloud-pc-settings"
description: "



In the previous articles, we covered the fundamentals of Windows 365 and walked through the deployment of a Windows 365 Enterprise environment.
Once your Cloud PCs are provisioned, the real..."
---

<audio controls style="width:100%"><source src="https://substack-post-media.s3.amazonaws.com/public/images/7bdfe9c9-6b7b-40eb-b072-884e154a05f5_2000x1125.jpeg" type="audio/mpeg"></audio>


<div class="captioned-image-container"><figure><a class="image-link image2" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!qyZx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!qyZx!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 424w, https://substackcdn.com/image/fetch/$s_!qyZx!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 848w, https://substackcdn.com/image/fetch/$s_!qyZx!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!qyZx!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!qyZx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":null,"width":null,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Understanding Cloud PC Settings","title":null,"type":null,"href":null,"belowTheFold":false,"topImage":true,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Understanding Cloud PC Settings" title="Windows 365 Wednesdays - Understanding Cloud PC Settings" srcset="https://substackcdn.com/image/fetch/$s_!qyZx!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 424w, https://substackcdn.com/image/fetch/$s_!qyZx!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 848w, https://substackcdn.com/image/fetch/$s_!qyZx!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!qyZx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c17884e-9323-46a0-8387-021f18093c66_2000x1125.jpeg 1456w" sizes="100vw" fetchpriority="high"></source></picture><div></div>
</div></a></figure></div>
<p>In the previous articles, we covered the <a href="https://burgerhou.tj/iigegb?ref=burgerhout.org">fundamentals of Windows 365</a> and walked through <a href="https://burgerhou.tj/sy6kj2?ref=burgerhout.org">the deployment of a Windows 365 Enterprise</a> environment.</p>
<p>Once your Cloud PCs are provisioned, the real management begins.</p>
<p>Unlike a traditional physical endpoint, Windows 365 provides several management actions that can significantly reduce support time and improve the end-user experience. Features like restoring a Cloud PC, resizing it to a more powerful SKU, or restarting it remotely are all available directly from Microsoft Intune.</p>
<p>In this article, we'll explore the most important Cloud PC management actions, explain when you should use them, and share a few best practices from real-world deployments.</p>
<p>We'll cover:</p>
<ul>
<li><p>Navigating to your Cloud PCs</p></li>
<li><p>Restarting a Cloud PC</p></li>
<li><p>Restoring a Cloud PC</p></li>
<li><p>Resizing a Cloud PC</p></li>
<li><p>Reviewing device information</p></li>
<li><p>Best practices</p></li>
</ul>
<h3>Where can you manage Cloud PCs?</h3>
<p>All Cloud PC-specific management actions are available from within Microsoft Intune.</p>
<p>Navigate to <strong>Devices</strong> → <strong>Manage Windows 365 Cloud PCs</strong> → <strong>All Cloud PCs</strong></p>
<p>Here you'll find an overview of every Cloud PC in your environment, including:</p>
<ul>
<li><p>Device name</p></li>
<li><p>Assigned user</p></li>
<li><p>Provisioning status</p></li>
<li><p>License type</p></li>
<li><p>Device health</p></li>
<li><p>Last sign-in</p></li>
<li><p>Provisioning policy</p></li>
</ul>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!ypYD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!ypYD!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 424w, https://substackcdn.com/image/fetch/$s_!ypYD!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 848w, https://substackcdn.com/image/fetch/$s_!ypYD!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!ypYD!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!ypYD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg" width="1384" height="694" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":694,"width":1384,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Understanding Cloud PC Settings","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Understanding Cloud PC Settings" title="Windows 365 Wednesdays - Understanding Cloud PC Settings" srcset="https://substackcdn.com/image/fetch/$s_!ypYD!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 424w, https://substackcdn.com/image/fetch/$s_!ypYD!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 848w, https://substackcdn.com/image/fetch/$s_!ypYD!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!ypYD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74557740-5b02-4b94-b574-c7435ca83ae2_1384x694.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a><figcaption class="image-caption">Figure 01 - Windows 365 – All Cloud PCs overview</figcaption></figure></div>
<p>Selecting a Cloud PC opens the device management page, where you'll find all available management actions.</p>
<h3>Restarting a Cloud PC</h3>
<p>Sometimes the simplest solution is still the best one. Whether a Windows Update requires a reboot or an application has become unresponsive, administrators can restart a Cloud PC without requiring the user to initiate the action.</p>
<h4>When should you use it?</h4>
<p>Typical scenarios include:</p>
<ul>
<li><p>Completing Windows Updates</p></li>
<li><p>Troubleshooting application issues</p></li>
<li><p>Refreshing system services</p></li>
<li><p>General maintenance</p></li>
</ul>
<h4>How to restart a Cloud PC</h4>
<ol>
<li><p>Open the <strong>Intune Admin Center</strong>.</p></li>
<li><p>Navigate to <strong>Devices</strong> → <strong>Manage Windows 365 Cloud PCs</strong> → <strong>All Cloud PCs</strong>.</p></li>
<li><p>Select the Cloud PC.</p></li>
<li><p>Click <strong>Restart</strong>.</p></li>
<li><p>Confirm the action.</p></li>
</ol>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!Sefb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!Sefb!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 424w, https://substackcdn.com/image/fetch/$s_!Sefb!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 848w, https://substackcdn.com/image/fetch/$s_!Sefb!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!Sefb!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!Sefb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg" width="1381" height="408" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/b6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":408,"width":1381,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Understanding Cloud PC Settings","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Understanding Cloud PC Settings" title="Windows 365 Wednesdays - Understanding Cloud PC Settings" srcset="https://substackcdn.com/image/fetch/$s_!Sefb!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 424w, https://substackcdn.com/image/fetch/$s_!Sefb!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 848w, https://substackcdn.com/image/fetch/$s_!Sefb!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!Sefb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f083c0-906e-48ef-88fe-e6ab849af0c7_1381x408.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a><figcaption class="image-caption">Figure 02 - Restarting a Cloud PC</figcaption></figure></div>
<div class="callout-block" data-callout="true"><p>💡Always inform users before restarting their Cloud PC. Although the action is quick, any unsaved work will be lost.</p></div>
<h3>Restoring a Cloud PC</h3>
<p>This is probably one of my favorite Windows 365 features. Instead of rebuilding an entire desktop after something goes wrong, you can restore the Cloud PC to an earlier restore point.<br>In many situations, this saves hours of troubleshooting.</p>
<h4>When should you use Restore?</h4>
<p>Examples include:</p>
<ul>
<li><p>A faulty software installation</p></li>
<li><p>Corrupted Windows components</p></li>
<li><p>Configuration changes causing instability</p></li>
<li><p>Testing software that didn't go as planned</p></li>
</ul>
<h4>How to restore a Cloud PC</h4>
<ol>
<li><p>Open <strong>Devices</strong> → <strong>Manage Windows 365 Cloud PCs</strong> → <strong>All Cloud PCs</strong>.</p></li>
<li><p>Select the Cloud PC.</p></li>
<li><p>Click <strong>Restore</strong>.</p></li>
<li><p>Select the desired restore point.</p></li>
<li><p>Click <strong>Restore</strong> again.</p></li>
<li><p>Confirm the action.</p></li>
</ol>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!vTam!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!vTam!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 424w, https://substackcdn.com/image/fetch/$s_!vTam!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 848w, https://substackcdn.com/image/fetch/$s_!vTam!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!vTam!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!vTam!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg" width="580" height="368" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":368,"width":580,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Understanding Cloud PC Settings","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Understanding Cloud PC Settings" title="Windows 365 Wednesdays - Understanding Cloud PC Settings" srcset="https://substackcdn.com/image/fetch/$s_!vTam!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 424w, https://substackcdn.com/image/fetch/$s_!vTam!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 848w, https://substackcdn.com/image/fetch/$s_!vTam!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!vTam!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F978fa562-7ab8-4c8d-9ad7-595ca083f729_580x368.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a><figcaption class="image-caption">Figure 03 - Available restore points</figcaption></figure></div>
<h4>Things to know</h4>
<ul>
<li><p>The operating system is restored to the selected point in time.</p></li>
<li><p>Applications installed after that restore point may need to be reinstalled.</p></li>
<li><p>Files stored in OneDrive remain unaffected.</p></li>
<li><p>Restore requires point-in-time restore to be configured/enabled first.</p></li>
</ul>
<div class="callout-block" data-callout="true"><p>💡Before reprovisioning a Cloud PC, always check whether a restore point can solve the problem first. It usually takes only a fraction of the time required to build a new Cloud PC.</p></div>
<h3>Resizing a Cloud PC</h3>
<p>Business requirements change, and so do user workloads. Fortunately, Windows 365 allows administrators to resize a Cloud PC without starting from scratch.</p>
<p>Whether a developer needs additional RAM or a project requires more processing power, resizing is a straightforward operation.</p>
<h4>Typical scenarios</h4>
<ul>
<li><p>Developers</p></li>
<li><p>Engineers</p></li>
<li><p>Designers</p></li>
<li><p>Temporary projects</p></li>
<li><p>Power users</p></li>
</ul>
<h4>How to resize a Cloud PC</h4>
<ol>
<li><p>Open <strong>Devices</strong> → <strong>Manage Windows 365 Cloud PCs</strong> → <strong>All Cloud PCs</strong>.</p></li>
<li><p>Select the Cloud PC.</p></li>
<li><p>Click <strong>Resize</strong>.</p></li>
<li><p>Choose one of the available license configurations.</p></li>
<li><p>Confirm the resize operation.</p></li>
</ol>
<h4>Things to know</h4>
<ul>
<li><p>Only supported upgrade paths are displayed.</p></li>
<li><p>The Cloud PC will restart during the resize.</p></li>
<li><p>User data and installed applications remain available.</p></li>
<li><p>Resize depends on available license inventory and Enterprise disk downgrades aren't supported.</p></li>
</ul>
<div class="callout-block" data-callout="true"><p>💡More CPU or memory isn't always the answer. Check Task Manager or Endpoint Analytics before assuming the Cloud PC needs a larger SKU.</p></div>
<h3>Reviewing Cloud PC information</h3>
<p>Every Cloud PC contains a wealth of operational information that can help administrators and helpdesk engineers troubleshoot issues.<br>Some of the most useful properties include:</p>
<ul>
<li><p>Provisioning Status</p></li>
<li><p>Device Health</p></li>
<li><p>Assigned User</p></li>
<li><p>Provisioning Policy</p></li>
<li><p>Cloud PC Size</p></li>
<li><p>Region</p></li>
<li><p>Last Sign-in</p></li>
<li><p>Device Name</p></li>
</ul>
<p>Knowing where to find this information can often save valuable troubleshooting time. You can find some overviews about the Cloud PCs at <strong>Reports</strong> → <strong>Windows 365</strong> → <strong>Windows 365 monitoring (prview)</strong> or <strong>Windows 365 overview</strong></p>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!vCfJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!vCfJ!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 424w, https://substackcdn.com/image/fetch/$s_!vCfJ!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 848w, https://substackcdn.com/image/fetch/$s_!vCfJ!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!vCfJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!vCfJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg" width="1381" height="1089" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":1089,"width":1381,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Understanding Cloud PC Settings","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Understanding Cloud PC Settings" title="Windows 365 Wednesdays - Understanding Cloud PC Settings" srcset="https://substackcdn.com/image/fetch/$s_!vCfJ!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 424w, https://substackcdn.com/image/fetch/$s_!vCfJ!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 848w, https://substackcdn.com/image/fetch/$s_!vCfJ!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!vCfJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84b0f91d-756a-42b6-b782-3aa8dd043bf6_1381x1089.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a><figcaption class="image-caption">Figure 04 - Windows 365 monitoring (preview)</figcaption></figure></div>
<div class="captioned-image-container"><figure><a class="image-link image2 is-viewable-img" target="_blank" href="https://substackcdn.com/image/fetch/%24s_!APzS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg" data-component-name="Image2ToDOM"><div class="image2-inset">
<picture><source type="image/webp" srcset="https://substackcdn.com/image/fetch/$s_!APzS!,w_424,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 424w, https://substackcdn.com/image/fetch/$s_!APzS!,w_848,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 848w, https://substackcdn.com/image/fetch/$s_!APzS!,w_1272,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!APzS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 1456w" sizes="100vw"><img src="https://substackcdn.com/image/fetch/%24s_!APzS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg" width="1381" height="1089" data-attrs='{"src":"https://substack-post-media.s3.amazonaws.com/public/images/744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":1089,"width":1381,"resizeWidth":null,"bytes":null,"alt":"Windows 365 Wednesdays - Understanding Cloud PC Settings","title":null,"type":null,"href":null,"belowTheFold":true,"topImage":false,"internalRedirect":null,"isProcessing":false,"align":null,"offset":false}' class="sizing-normal" alt="Windows 365 Wednesdays - Understanding Cloud PC Settings" title="Windows 365 Wednesdays - Understanding Cloud PC Settings" srcset="https://substackcdn.com/image/fetch/$s_!APzS!,w_424,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 424w, https://substackcdn.com/image/fetch/$s_!APzS!,w_848,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 848w, https://substackcdn.com/image/fetch/$s_!APzS!,w_1272,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 1272w, https://substackcdn.com/image/fetch/$s_!APzS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F744ab11c-68ae-47ce-915d-cd86e69288ac_1381x1089.jpeg 1456w" sizes="100vw" loading="lazy"></source></picture><div class="image-link-expand"><div class="pencraft pc-display-flex pc-gap-8 pc-reset">
<button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container restack-image"><svg aria-hidden="true" width="20" height="20" viewbox="0 0 20 20" fill="none" stroke-width="1.5" stroke="var(--color-fg-primary)" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><g><path d="M2.53001 7.81595C3.49179 4.73911 6.43281 2.5 9.91173 2.5C13.1684 2.5 15.9537 4.46214 17.0852 7.23684L17.6179 8.67647M17.6179 8.67647L18.5002 4.26471M17.6179 8.67647L13.6473 6.91176M17.4995 12.1841C16.5378 15.2609 13.5967 17.5 10.1178 17.5C6.86118 17.5 4.07589 15.5379 2.94432 12.7632L2.41165 11.3235M2.41165 11.3235L1.5293 15.7353M2.41165 11.3235L6.38224 13.0882"></path></g></svg></button><button tabindex="0" type="button" class="pencraft pc-reset pencraft icon-container view-image"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewbox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-maximize2 lucide-maximize-2"><polyline points="15 3 21 3 21 9"></polyline><polyline points="9 21 3 21 3 15"></polyline><line x1="21" x2="14" y1="3" y2="10"></line><line x1="3" x2="10" y1="21" y2="14"></line></svg></button>
</div></div>
</div></a><figcaption class="image-caption">Figure 05 - Windows 365 overview</figcaption></figure></div>
<h3>Best Practices</h3>
<p>After working with Windows 365 in several customer environments, a few recommendations consistently stand out.</p>
<h4>Keep your Cloud PCs standardized</h4>
<p>Avoid creating unnecessary image variations or provisioning policies.<br>The more standardized your environment is, the easier it becomes to manage.</p>
<h4>Use Restore before Reprovision</h4>
<p>Reprovisioning should not be your first reaction.<br>Whenever possible, try a Restore first.</p>
<h4>Resize only when necessary</h4>
<p>A larger Cloud PC also means higher licensing costs.<br>Validate whether the bottleneck is actually hardware-related before upgrading.</p>
<h4>Manage Cloud PCs like any other endpoint</h4>
<p>Windows 365 doesn't require a completely new management strategy.</p>
<p>Continue using:</p>
<ul>
<li><p>Configuration Profiles</p></li>
<li><p>Compliance Policies</p></li>
<li><p>Security Baselines</p></li>
<li><p>Application Deployment</p></li>
<li><p>Windows Autopatch / Windows Update policies</p></li>
</ul>
<p>A Cloud PC is simply another Windows endpoint managed through Intune.</p>
<h3>Final Thoughts</h3>
<p>Provisioning a Cloud PC is only the beginning.</p>
<p>Windows 365 includes several management capabilities that can significantly reduce operational overhead while improving the end-user experience.</p>
<p>Understanding features like Restart, Restore, and Resize enables administrators to resolve issues more quickly and keep users productive with minimal disruption.</p>
<p>In the next part of this series, we'll look at <strong>Windows Autopatch</strong> and explore how to keep Cloud PCs secure, compliant, and automatically up to date.</p>
<p>That is it for now. Until next time. 👋</p>


[Listen on Substack](https://www.burgerhout.org/p/windows-365-wednesdays-understanding-cloud-pc-settings)
